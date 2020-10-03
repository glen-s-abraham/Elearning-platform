from rest_framework import serializers
from lessonsApp.models import Lessons

class LessonsSerializer(serializers.ModelSerializer):
	"""Serializer for lessons"""
	class Meta:
		model=Lessons
		fields='__all__'