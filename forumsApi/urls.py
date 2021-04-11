from django.urls import path,include
from rest_framework.routers import DefaultRouter
from forumsApi.views import ThreadsView
from forumsApi.views import RepliesView
from assignmentsApi.views import SubmissionsView


router=DefaultRouter()
router.register('threads',ThreadsView)
router.register('replies',RepliesView)


urlpatterns=[
	path('',include(router.urls)),
	
]
#path('submissions/',SubmissionsView.as_view())