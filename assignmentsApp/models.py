from django.db import models
from userApp.models import User
from datetime import datetime

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

class Assignments(models.Model):
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	topic=models.CharField(max_length=500,blank=False)
	course=models.CharField(max_length=20,choices=course_choices,default='BSC.CS')
	semester=models.CharField(max_length=3,choices=semester_choices,default='S1')
	date = models.DateTimeField(default=datetime.now, blank=True)
	
	
	def __str__(self):
		return str(self.topic)

class Submissions(models.Model):
	assignment=models.ForeignKey(Assignments, on_delete=models.CASCADE)
	submitted_by=models.ForeignKey(User, on_delete=models.CASCADE)
	file = models.FileField(upload_to='Assignments/')
	date = models.DateTimeField(default=datetime.now, blank=True)
	
	
	def __str__(self):
		return str(self.submitted_by)