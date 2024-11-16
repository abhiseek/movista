"""
URL configuration for movie project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from app1 import views

app_name="app1"

urlpatterns = [
    # path('',views.home,name="home"),
    path('',views.Index.as_view(),name="home"),
    # path('add/',views.add,name="add"),
    # path('addmovies/', views.addmovies, name="addmovies"),
path('addmovies/', views.Addmovie.as_view(), name="addmovies"),
    # path('detail/<int:i>',views.detail,name="detail"),

    path('movie/<int:pk>', views.Detail.as_view(), name="detail"),#pk -primary key for generic purpose
    # path('delete/<int:i>',views.delete,name="delete"),
    path('delete/<int:pk>',views.Delete.as_view(),name="delete"),
    # path('edit/<int:i>',views.edit,name="edit"),
    path('edit/<int:pk>',views.Update.as_view(),name="edit"),

]

