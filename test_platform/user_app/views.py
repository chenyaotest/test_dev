from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
#主要代码逻辑


def index(request):
    #print(request.method)
    #print(request.path)
    return render(request, "index.html")

#处理登录请求
def login_action(request):
    if request.method == "GET":
     username = request.GET.get("username")
     password = request.GET.get("password")
     if username == "" or password == "":
         #return HttpResponse("用户名或密码为空")
         return render(request, "index.html",
                       {"error":"用户名或密码错误"})