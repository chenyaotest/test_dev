from django.contrib import admin
from user_app.models import Project, Module

# Register your models here.
# django自带一个admin后台


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'status', 'create_time', 'id']
    search_fields = ['name']  # 搜索栏
    list_filter = ['status']  # 过滤器


class ModuleAdmin(admin.ModelAdmin):
    list_display = ['name', 'describe', 'create_time', 'project', 'id']
    search_fields = ['name']  # 搜索栏


admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)
