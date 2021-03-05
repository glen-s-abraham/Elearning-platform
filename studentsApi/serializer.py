from rest_framework import serializers
from userApp.models import User

class UserProfileSerializer(serializers.ModelSerializer):
	"""Serializer for User profile"""
	class Meta:
		model=User
		fields=('id','email','name','course','semester','password')
		extra_kwargs={
			'password':{
						'write_only':False,
						'style':{'input_type':'password'}
			}
		}
		
	def create(self,validated_data):	
		user=User.Objects.create_user(
				email=validated_data['email'],
				name=validated_data['name'],
				course=validated_data['course'],
				semester=validated_data['semester'],
				password=validated_data['password']
					
				)
			

		return user