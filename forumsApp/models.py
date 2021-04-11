from django.db import models
from userApp.models import User


class Threads(models.Model):
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	subject=models.CharField(max_length=100)
	descreption=models.CharField(max_length=500)
	file = models.FileField(upload_to='Forums/',null=True,blank=True)
	def __str__(self):
		return str(self.subject)

class Replies(models.Model):
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	thread=models.ForeignKey(Threads, on_delete=models.CASCADE)
	reply=models.CharField(max_length=1000)
	file = models.FileField(upload_to='Forums/',null=True,blank=True)
	def __str__(self):
		return str(self.thread)		
