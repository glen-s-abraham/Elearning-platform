from django.forms import ModelForm
from .models import Assignments

class AssignmentsForm(ModelForm):
	class Meta:
		model = Assignments
		fields = ['topic','course', 'semester']