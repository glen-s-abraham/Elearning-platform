from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


course_choices=semester_choices=[
		('BSC.CS','Bsc computerScience'),
		('MSC.CS','Msc computerScience'),
		]
semester_choices=[
		('S1','semester 1'),
		('S2','semester 2'),
		('S3','semester 3'),
		('S4','semester 4'),
		('S5','semester 5'),
		('S6','semester 6')
		]




class UserManager(BaseUserManager):
	"""Manager class for user profile"""
	def create_user(self,email,name,course,semester,password=None):
		if not email:
			raise ValueError("User must have email")
		email=self.normalize_email(email)
		user=self.model(email=email,name=name,course=course,semester=semester)
		user.set_password(password)
		user.save(using=self.db)
		return user

	def create_superuser(self,email,name,password):
		user=self.create_user(email=email,name=name,course=None,semester=None,password=password)
		user.is_superuser=True
		user.is_staff=True
		user.save(using=self._db)
		return user	

class User(AbstractBaseUser,PermissionsMixin):
	"""Model for the user profile class"""
	email=models.EmailField(max_length=255,unique=True)
	name=models.CharField(max_length=255,unique=True)
	course=models.CharField(max_length=20,choices=course_choices,default='BSC.CS',null=True)
	semester=models.CharField(max_length=3,choices=semester_choices,default='S1',null=True)
	is_active=models.BooleanField(default=True)
	is_staff=models.BooleanField(default=False)
	is_superuser=models.BooleanField(default=False)
	Objects=UserManager()
	USERNAME_FIELD='name'
	REQUIRED_FIELDS=['email']		

	