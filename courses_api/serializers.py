from rest_framework import serializers
from coursesApp.models import Courses

class CoursesSerializer(serializers.ModelSerializer):
	"""Serializer for listing the various Courses"""
	class Meta:
		model=Courses
		fields='__all__'
