from django.contrib import admin
from django.urls import path

from assignmentsApp.views import AssignmentsView as av
from assignmentsApp.views import AssignmentsCreateView as ac
from assignmentsApp.views import AssignmentsUpdateView as au
from assignmentsApp.views import AssignmentsDeleteView as ad
from assignmentsApp.views import submissions

urlpatterns = [
    path('', av.as_view(),name="assignments"),
    path('createAssignment/', ac.as_view(),name="createAssignment"),
    path('<int:id>/updateAssignment/',au.as_view() ,name="updateAssignment"),
    path('<int:id>/deleteAssignment/', ad.as_view(),name="deleteAssignment"),
     path('submissions/', submissions,name="submissions"),
    
    
]
"""path('', cv.as_view(),name="courses"),
    path('createCourse/', cc.as_view(),name="createCourse"),
    path('<int:id>/',cld.as_view() ,name="detailCourse"),
    path('<int:id>/updateCourse/',cu.as_view() ,name="updateCourse"),
    path('<int:id>/deleteCourse/', cd.as_view(),name="deleteCourse"),"""