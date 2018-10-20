from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from project_app.forms import ModuleForm
from project_app.models import Project, Module


@login_required  # 判断用户是否登录
def module_manage(request):
    username = request.session.get('user', '')  # 读取浏览器 session
    module_all = Module.objects.all()
    # print(project_all)
    return render(request, "module_manage.html", {"user": username, "modules": module_all, "type": "list"})


@login_required
def add_module(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ModuleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            project = form.cleaned_data['project']
            Module.objects.create(name=name, describe=describe, project=project)
            # redirect to a new URL:
            return HttpResponseRedirect('/manage/module_manage/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ModuleForm()

    return render(request, 'module_manage.html', {'form': form, "type": "add"})


@login_required
def edit_module(request, mid):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ModuleForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            name = form.cleaned_data['name']
            describe = form.cleaned_data['describe']
            project = form.cleaned_data['project']

            Module.objects.select_for_update().filter(id=mid).update(name=name, describe=describe, project=project)
            # redirect to a new URL:
            return HttpResponseRedirect('/manage/module_manage/')
    else:
        if mid:
            form = ModuleForm(instance=Module.objects.get(id=mid))
        else:
            form = ModuleForm()

    return render(request, 'module_manage.html', {
        "form": form,
        "type": "edit",
        "mid": mid,
    })


@login_required
def delete_module(request, mid):
    if mid:
        Module.objects.get(id=mid).delete()
    return HttpResponseRedirect('/manage/module_manage/')
