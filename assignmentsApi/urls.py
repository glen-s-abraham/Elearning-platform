from django.urls import path,include
from rest_framework.routers import DefaultRouter
from assignmentsApi.views import PendingAssignmentsView
from assignmentsApi.views import CompletedAssignmentsView
from assignmentsApi.views import SubmissionsView


router=DefaultRouter()
router.register('pending',PendingAssignmentsView)
router.register('completed',CompletedAssignmentsView)


urlpatterns=[
	path('',include(router.urls)),
	path('submissions/',SubmissionsView.as_view())
]