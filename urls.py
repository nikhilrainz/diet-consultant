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
from django.conf import settings
from django.conf.urls.static import static
from mydiet import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('index/', views.index),
    path('expert/', views.expert),
    path('dietandnutrition/', views.dietandnutrition),
    path('article/', views.article),
    path('reviews/', views.reviews),

    path('userreg/', views.user_register),
    path('expert_register/', views.expert_register),
    path('login/', views.login),

    path('user_profile/', views.user_profile),
    path('user_home/', views.user_home),
    path('userchangepass/',views.userchangepass),
    path('edit/<email>', views.edit),
    path('update/<email>', views.update),
    path('user_dn/', views.user_dn),
    path('user_advise/', views.user_advise),
    path('user_result/', views.user_result),
    path('user_report/', views.user_report),
    path('user_doctor/', views.user_doctor),
    path('user_expertview/', views.user_expertview),
    path('userpost/', views.userpost),
    path('userpreview1/', views.userpreview_1),
    path('get-userchat-msg/', views.get_userchat_msg),
    path('chatpreview/',views.chatpreview),
    path('user_chathistory/',views.user_chathistory),
    path('user_chatpreview/', views.user_chatpreview),
    path('user_chatp/', views.user_chatp),
    path('user_articles/', views.user_articles),
    path('user_feedback/', views.user_feedback),

    path('expert_home/', views.expert_home),
    path('expert_profile/', views.expert_profile),
    path('editprofile/<email>', views.editprofile),
    path('update_expert/<email>', views.update_expert),
    path('expert_doctor/', views.expert_doctor),
    path('expert_dn/', views.expert_dn),
    path('expert_articles/', views.expert_articles),
    path('expertpost/', views.expertpost),
    path('expert_viewreq/', views.expert_viewreq),
    path('expertpreview1/', views.expertpreview_1),
    path('get-chat-msg/', views.get_chat_msg),
    path('expert_chat/', views.expertpost),
    path('expert_viewreport/', views.expert_viewreport),
    path('admin_home/', views.admin_home),
    path('admin_user/', views.admin_user),
    path('admin_doctor/', views.admin_doctor),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
