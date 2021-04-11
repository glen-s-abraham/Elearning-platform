from rest_framework import serializers
from assignmentsApp.models import Assignments
from assignmentsApp.models import Submissions

class AssignmentsSerializer(serializers.ModelSerializer):
	"""Serializer for listing the various Courses"""
	class Meta:
		model=Assignments
		fields=('id','topic','course','semester','date','author')

class SubmissionsSerializer(serializers.Serializer):
	aid=serializers.IntegerField()
	file = serializers.FileField()
	
    
		

	