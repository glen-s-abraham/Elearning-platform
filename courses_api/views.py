from rest_framework import viewsets
from courses_api.serializers import CoursesSerializer
from rest_framework.permissions import IsAuthenticated
from courses_api import permissions
from rest_framework.authentication import TokenAuthentication
from coursesApp.models import Courses


class CoursesView(viewsets.ModelViewSet):
	serializer_class=CoursesSerializer
	queryset=Courses.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes=(permissions.IsAdminUser,IsAuthenticated)

	def get_queryset(self):
		"""Filter courses on streams and semester"""
		
		user=self.request.user
		stream = user.course
		sem = user.semester
		return Courses.objects.filter(course=stream,semester=sem)
		

