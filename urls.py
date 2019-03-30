"""dietandnutritionadvisor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from mydiet import views

urlpatterns = [
    path('admin/', admin.site.urls),
path('index/', views.index),
    path('expert/', views.expert),
    path('dietandnutrition/', views.dietandnutrition),
    path('article/', views.article),
    path('contact/', views.contact),

    path('userreg/', views.user_register),
    path('expert_register/', views.expert_register),
    path('login/', views.login),

    path('user_profile/', views.user_profile),
    path('user_home/', views.user_home),
    path('user_dn/', views.user_dn),
    path('user_advise/', views.user_advise),
    path('user_result/', views.user_result),
    path('user_articles/', views.user_articles),

    path('expert_home/', views.expert_home),
    path('expert_profile/', views.expert_profile),
    path('expert_doctor/', views.expert_doctor),
    path('expert_dn/', views.expert_dn),
    path('expert_articles/', views.expert_articles),
    path('expert_viewreq/', views.expert_viewreq),
    path('expert_reply/', views.expert_reply),

    path('admin_home/', views.admin_home),
    path('admin_user/', views.admin_user),
    path('admin_userview/', views.admin_userview),
    path('admin_doctor/', views.admin_doctor),
    path('admin_viewexpert/', views.admin_viewexpert)
]
