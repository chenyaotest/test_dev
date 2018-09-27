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
        print(username)
        print(type(username))
        print(password)
        print(type(password))
        if username == "" or password == "":
            return render(request, "index.html", {"error": "用户名或密码为空"})
        else:
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                auth.login(request, user)  # 验证登录
                return render(request, "project_manage.html")
            else:
                return render(request, "index.html", {"error": "用户名或密码错误"})
