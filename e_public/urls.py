"""e_public URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from e_public_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.signup,name="signup"),
    path("home",views.home,name="home"),
    path("dep_signup",views.dep_signup,name="dep_signup"),
    path("user_add_complaint",views.user_add_complaint,name="user_add_complaint"),
    path("admin_home",views.admin_home,name="admin_home"),
    path("admin_view_complaints",views.admin_view_complaints,name="admin_view_complaints"),
    path("admin_approve_complaint/<str:complaint_id>",views.admin_approve_complaint,name="admin_approve_complaint"),
    path("approved_complaints",views.approved_complaints,name="approved_complaints"),
    path("admin_disapprove_complaint/<str:complaint_id>",views.admin_disapprove_complaint,name="admin_disapprove_complaint"),


    path("dep_view_complaint",views.dep_view_complaint,name="dep_view_complaint"),
    path("complaint_complete/<str:complaint_id>",views.complaint_complete,name="complaint_complete"),



    path("dep_login",views.dep_login,name="dep_login"),
    path("dep_home",views.dep_home,name="dep_home"),

    path("user_home",views.user_home,name="user_home"),
    path("user_complaint_status",views.user_complaint_status,name="user_complaint_status"),
    path("user_approve_solution/<str:complaint_id>",views.user_approve_solution,name="user_approve_solution"),












]
