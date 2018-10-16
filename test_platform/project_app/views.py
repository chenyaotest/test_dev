from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from project_app.models import Project


@login_required  # 判断用户是否登录
def project_manage(request):
    username = request.session.get('user', '')  # 读取浏览器 session
    project_all = Project.objects.all()
    # print(project_all)
    return render(request, "project_manage.html", {"user": username, "projects": project_all, "type": "list"})


def add_project(request):
    username = request.session.get('user', '')  # 读取浏览器 session
    project_all = Project.objects.all()
    # print(project_all)
    return render(request, "project_manage.html", {"type": "add"})
