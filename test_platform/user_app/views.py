from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
# Create your views here.
# 主要代码逻辑


def index(request):
    # print(request.method)
    # print(request.path)
    return render(request, "index.html")


# 处理登录请求
def login_action(request):
    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        # print(username)
        # print(type(username))
        # print(password)
        # print(type(password))
        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名或密码为空"})
        else:
            user = auth.authenticate(username=username, password=password) # 记录用户登录状态
            if user is not None:
                auth.login(request, user)  # 验证登录
                request.session['user'] = username
                return HttpResponseRedirect('/manage/project_manage/')
                # return render(request, "project_manage.html")
            else:
                return render(request, "index.html", {"error": "用户名或密码错误"})
    else:
        return render(request, "index.html")

@login_required
def logout(request):
    auth.logout(request)  # 清除用户登录状态
    response = HttpResponseRedirect('/')
    return response

