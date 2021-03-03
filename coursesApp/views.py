from django.shortcuts import get_object_or_404

from coursesApp.models import Courses
from coursesApp.forms import CoursesForm

from .forms import CoursesForm
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
class CoursesView(ListView):
	model=Courses

	def get_queryset(self):
		user=self.request.user
		queryset=Courses.objects.filter(author=user.id)
		return queryset

@method_decorator(login_required(login_url='/users/'), name='dispatch')
class CoursesDetailView(DetailView):
	model=Courses

	def get_object(self):
		id=self.kwargs.get("id")
		return get_object_or_404(Courses,id=id)


		
@method_decorator(login_required(login_url='/users/'), name='dispatch')	
class CoursesCreateView(CreateView):
	model=Courses
	form_class=CoursesForm
	success_url='/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)
        
@method_decorator(login_required(login_url='/users/'), name='dispatch')	
class CoursesUpdateView(UpdateView):

	model=Courses
	form_class=CoursesForm
	template_name_suffix = '_update_form'
	success_url='/'

	def get_object(self):
		id=self.kwargs.get("id")
		return get_object_or_404(Courses,id=id)



@method_decorator(login_required(login_url='/users/'), name='dispatch')
class CoursesDeleteView(DeleteView):
	model=Courses
	template_name_suffix = '_delete'
	success_url='/'

	def get_object(self):
		id=self.kwargs.get("id")
		return get_object_or_404(Courses,id=id)		

	

	



    
    
   
	


			


