from rest_framework import viewsets
from courses_api.serializers import CoursesSerializer

from courses_api import permissions

from coursesApp.models import Courses


class CoursesView(viewsets.ModelViewSet):
	serializer_class=CoursesSerializer
	queryset=Courses.objects.all()
	permission_classes=(permissions.IsAdminUser,)

	def get_queryset(self):
		"""Filter courses on streams and semester"""
		streams=["MSC.CS","BSC.CS"]
		semesters=["S1","S2","S3","S4","S5","S6"]

		stream = self.request.query_params.get('stream', None)
		sem = self.request.query_params.get('sem', None)

		if stream in streams and sem in semesters:
			return Courses.objects.filter(course=stream,semester=sem)

		return Courses.objects.all()	


