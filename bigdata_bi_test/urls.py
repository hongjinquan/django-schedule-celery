"""bigdata_bi_test URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('task/one/', views.task_test_one),
    path('task/two/', views.task_test_two),
    path('task/three/', views.task_test_three),
    path('task/add/', views.task_test_create),
    path('task/stop/', views.task_test_stop),
    path('task/restart/', views.task_test_restart),
    path('task/del/', views.task_test_del),
    path('task/nums/', views.task_nums)
]
