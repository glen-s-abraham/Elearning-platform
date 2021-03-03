from django.db import models
from django.contrib.auth.models import User
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

class Courses(models.Model):
	author=models.ForeignKey(User, on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	course=models.CharField(max_length=20,choices=course_choices,default='BSC.CS')
	semester=models.CharField(max_length=3,choices=semester_choices,default='S1')
	cover = models.FileField(upload_to='Courses/',null=True,blank=True)
	def __str__(self):
		return str(self.title)




		
		
		

