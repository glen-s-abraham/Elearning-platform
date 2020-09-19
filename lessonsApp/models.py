from django.db import models
from coursesApp.models import Courses

class Lessons(models.Model):
	course=models.ForeignKey(Courses, on_delete=models.CASCADE)
	lessonname=models.CharField(max_length=100,unique=False)
	lesson = models.FileField(upload_to='Lessons/')
	def __str__(self):
		return str(self.lessonname)	