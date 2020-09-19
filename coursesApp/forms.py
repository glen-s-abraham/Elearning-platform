from django.forms import ModelForm
from .models import Courses

class CoursesForm(ModelForm):
	class Meta:
		model = Courses
		fields = ['title', 'course', 'semester']
	





        
        
