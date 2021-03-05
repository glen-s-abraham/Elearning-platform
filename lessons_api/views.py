from rest_framework import viewsets
from lessonsApp.models import Lessons
from lessons_api.serializers import LessonsSerializer 
from rest_framework.permissions import IsAuthenticated
from courses_api import permissions
from rest_framework.authentication import TokenAuthentication

# Create your views here.
class LessonsView(viewsets.ModelViewSet):
	serializer_class=LessonsSerializer
	authentication_classes = (TokenAuthentication,)
	queryset=Lessons.objects.all()
	permission_classes=(permissions.IsAdminUser,IsAuthenticated)
	

	def get_queryset(self):
		"""Filter courses on streams and semester"""
		course = self.request.query_params.get('cid', None)		
		if course:
			return Lessons.objects.filter(course=course)
		return None	