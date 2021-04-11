from rest_framework import viewsets
from rest_framework.views import APIView
from forumsApi.serializer import ThreadsSerializer
from forumsApi.serializer import RepliesSerializer
from rest_framework.permissions import IsAuthenticated
from forumsApi import permissions
from rest_framework.parsers import FileUploadParser
from rest_framework.authentication import TokenAuthentication
from forumsApp.models import Threads
from forumsApp.models import Replies
from userApp.models import User
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

class ThreadsView(viewsets.ModelViewSet):
	serializer_class=ThreadsSerializer
	queryset=Threads.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes=(IsAuthenticated,)

	def perform_create(self,serializer):

		print(serializer.validated_data)
		serializer.save(author=self.request.user)

class RepliesView(viewsets.ModelViewSet):
	serializer_class=RepliesSerializer
	queryset=Replies.objects.all()
	authentication_classes = (TokenAuthentication,)
	permission_classes=(IsAuthenticated,)

	def get_queryset(self):
		"""Filter courses on streams and semester"""
		thread = self.request.query_params.get('tid', None)		
		if thread:
			return Replies.objects.filter(thread=thread)
		return None	

	def perform_create(self,serializer):
		serializer.save(author=self.request.user)	
						
		
