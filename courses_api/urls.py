from django.urls import path,include
from rest_framework.routers import DefaultRouter
from courses_api.views import CoursesView


router=DefaultRouter()
router.register('',CoursesView)


urlpatterns=[
	path('',include(router.urls)),
]