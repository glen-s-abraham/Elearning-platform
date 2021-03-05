from django.urls import path,include
from rest_framework.routers import DefaultRouter
from lessons_api.views import LessonsView


router=DefaultRouter()
router.register('',LessonsView)



urlpatterns=[
	path('',include(router.urls)),
]