from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from project_app.forms import ProjectForm
from project_app.models import Project


@login_required  # 判断用户是否登录
def project_manage(request):
    username = request.session.get('user', '')  # 读取浏览器 session
    project_all = Project.objects.all()
    # print(project_all)
    return render(request, "project_manage.html", {"user": username, "projects": project_all, "type": "list"})


@login_required
def add_project(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']
            Project.objects.create(name=name, describe=describe, status=status)
            # redirect to a new URL:
            return HttpResponseRedirect('/manage/project_manage/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ProjectForm()

    return render(request, 'project_manage.html', {'form': form, "type": "add"})


@login_required
def edit_project(request, pid):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ProjectForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            status = form.cleaned_data['status']

            Project.objects.select_for_update().filter(id=pid).update(name=name, describe=describe, status=status)
            # redirect to a new URL:
            return HttpResponseRedirect('/manage/project_manage/')
    else:
        if pid:
            form = ProjectForm(instance=Project.objects.get(id=pid))
        else:
            form = ProjectForm()

    return render(request, 'project_manage.html', {
        "form": form,
        "type": "edit",
        "pid": pid,
    })


@login_required
def delete_project(request, pid):
    if pid:
        Project.objects.get(id=pid).delete()
    return HttpResponseRedirect('/manage/project_manage/')
