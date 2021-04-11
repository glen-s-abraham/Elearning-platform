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
from forumsApp.views import ThreadsView as tv
from forumsApp.views import MyThreadsView as mtv
from forumsApp.views import ThreadsCreateView as tc
from forumsApp.views import ThreadsUpdateView as tu
from forumsApp.views import ThreadsDeleteView as td
from forumsApp.views import replies
from forumsApp.views import RepliesDeleteView as rd

urlpatterns = [
    path('', tv.as_view(),name="threads"),
    path('myThreads/', mtv.as_view(),name="myThreads"),
    path('createThread/', tc.as_view(),name="createThread"),
    path('<int:id>/updateThread/',tu.as_view() ,name="updateThread"),
    path('<int:id>/deleteThread/',td.as_view() ,name="deleteThread"),
    path('replies/', replies,name="replies"),
    path('<int:tid>/<int:rid>/deleteReply/',rd.as_view() ,name="deleteReply"),


    
    
]

"""path('createCourse/', cc.as_view(),name="createCourse"),
    path('<int:id>/',cld.as_view() ,name="detailCourse"),
    path('<int:id>/updateCourse/',cu.as_view() ,name="updateCourse"),
    path('<int:id>/deleteCourse/', cd.as_view(),name="deleteCourse"),"""