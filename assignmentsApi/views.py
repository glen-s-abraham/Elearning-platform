from rest_framework import viewsets
from rest_framework.views import APIView
from assignmentsApi.serializer import AssignmentsSerializer
from assignmentsApi.serializer import SubmissionsSerializer
from rest_framework.permissions import IsAuthenticated
from assignmentsApi import permissions
from rest_framework.parsers import FileUploadParser
from rest_framework.authentication import TokenAuthentication
from assignmentsApp.models import Assignments
from assignmentsApp.models import Submissions
from userApp.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404


class PendingAssignmentsView(viewsets.ModelViewSet):
	serializer_class=AssignmentsSerializer
	queryset=Assignments.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes=(permissions.IsAdminUser,IsAuthenticated)

	def get_queryset(self):
		"""Filter assignments on streams and semester"""
		
		user=self.request.user
		stream = user.course
		sem = user.semester
		submissions=Submissions.objects.values('assignment').filter(submitted_by=user)
		assignments=Assignments.objects.exclude(id__in=submissions).filter(course=stream,semester=sem)


					
		print(submissions)	
		
		return assignments

class CompletedAssignmentsView(viewsets.ModelViewSet):
	serializer_class=AssignmentsSerializer
	queryset=Assignments.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes=(permissions.IsAdminUser,IsAuthenticated)

	def get_queryset(self):
		"""Filter assignments on streams and semester"""
		
		user=self.request.user
		stream = user.course
		sem = user.semester
		submissions=Submissions.objects.values('assignment').filter(submitted_by=user)
		assignments=Assignments.objects.filter(id__in=submissions,course=stream,semester=sem)
		return assignments		

class SubmissionsView(APIView):
	authentication_classes = (TokenAuthentication,)
	permission_classes=(IsAuthenticated,)
	parser_class=(FileUploadParser,)
	serializer_class=SubmissionsSerializer
	def post(self,request):
		user=User.Objects.get(pk=self.request.user.id)
		aid=self.request.POST.get('aid')
		file=request.FILES.get('file')
		if aid and file:
			assignment=get_object_or_404(Assignments,pk=aid)
			try:
				print("try")
				submission=Submissions.objects.get(assignment=assignment,submitted_by=user)
				submission.file=file
				submission.save()

			except:
				submission=Submissions.objects.create(assignment=assignment,submitted_by=user,file=file)
				return Response({"message":"Submitted"})
		return Response({"message":'invalid'})

					
			
		
				