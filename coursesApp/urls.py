"""ELearn URL Configuration

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
from coursesApp.views import CoursesView as cv
from coursesApp.views import CoursesDetailView as cld
from coursesApp.views import CoursesCreateView as cc
from coursesApp.views import CoursesUpdateView as cu
from coursesApp.views import CoursesDeleteView as cd
urlpatterns = [
    path('', cv.as_view(),name="courses"),
    path('createCourse/', cc.as_view(),name="createCourse"),
    path('<int:id>/',cld.as_view() ,name="detailCourse"),
    path('<int:id>/updateCourse/',cu.as_view() ,name="updateCourse"),
    path('<int:id>/deleteCourse/', cd.as_view(),name="deleteCourse"),
    
    
]

"""path('createCourse/', views.createCourse,name="createCourse"),
    path('updateCourse/', views.updateCourse,name="updateCourse"),
    path('deleteCourse/', views.deleteCourse,name="deleteCourse"),"""