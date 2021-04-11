from rest_framework import serializers
from forumsApp.models import Threads
from forumsApp.models import Replies

class ThreadsSerializer(serializers.ModelSerializer):
	"""Serializer for listing the various Courses"""
	class Meta:
		model=Threads
		fields=('id','subject','descreption','file','author')

class RepliesSerializer(serializers.ModelSerializer):
	class Meta:
		model=Replies
		fields='__all__'
	
    
		

	