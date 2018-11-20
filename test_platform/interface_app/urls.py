from django.urls import path
from interface_app import views

urlpatterns = [

    # 项目管理
    path('case_manage/', views.case_manage),
    path('add_case/', views.add_case),
    path('api_debug/', views.api_debug),
    path('save_case/', views.save_case),
    path('get_project_list/', views.get_project_list),
    path('search_case_name/', views.search_case_name),
    path('debug_case/<int:cid>/', views.debug_case),
    path('delete_case/<int:cid>/', views.delete_case),
    path('get_case_info/', views.get_case_info),
    path('api_assert/', views.api_assert),
]
