from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404

from assignmentsApp.models import Assignments
from assignmentsApp.models import Submissions
from assignmentsApp.forms import AssignmentsForm


from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView  
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

#CRUD Functionality for Courses

@method_decorator(login_required(login_url='/users/'), name='dispatch')
class AssignmentsView(ListView):
	model=Assignments

	def get_queryset(self):
		user=self.request.user
		queryset=Assignments.objects.filter(author=user.id)
		return queryset

@method_decorator(login_required(login_url='/users/'), name='dispatch')	
class AssignmentsCreateView(CreateView):
	model=Assignments
	form_class=AssignmentsForm
	success_url='/assignments/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)		

@method_decorator(login_required(login_url='/users/'), name='dispatch')	
class AssignmentsUpdateView(UpdateView):

	model=Assignments
	form_class=AssignmentsForm
	success_url='/assignments/'

	def get_object(self):
		id=self.kwargs.get("id")
		return get_object_or_404(Assignments,id=id)		

@method_decorator(login_required(login_url='/users/'), name='dispatch')	
class AssignmentsDeleteView(DeleteView):

	model=Assignments
	template_name_suffix = '_delete'
	success_url='/assignments/'

	def get_object(self):
		id=self.kwargs.get("id")
		return get_object_or_404(Assignments,id=id)			


@login_required(login_url='login')
def submissions(request):
    aid=request.GET['aid']
    assignment=Assignments.objects.get(pk=aid)
    submissions=Submissions.objects.filter(assignment=assignment)
    context={'assignment':assignment,'submissions':submissions}		
    return render(request,'assignmentsApp/submissions_list.html',context)		