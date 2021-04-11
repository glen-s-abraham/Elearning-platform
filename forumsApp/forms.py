from django.forms import ModelForm
from forumsApp.models import Threads
from forumsApp.models import Replies

class ThreadsForm(ModelForm):
	class Meta:
		model = Threads
		fields = ['subject','descreption', 'file']

class RepliesForm(ModelForm):
	class Meta:
		model = Replies
		fields = ['reply', 'file']		