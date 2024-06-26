from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path('',views.index,name="home"),
    path('login',views.loginUser,name="login"),
    path('logout',views.logoutUser,name="logout"),
    path('create',views.create,name="create"),
    path('adminpage',views.adminpage,name="adminpage"),
    path('userpage',views.userpage,name="userpage")
]