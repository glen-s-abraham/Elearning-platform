from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from lessonsApp.models import Lessons
from coursesApp.models import Courses
from django.contrib.auth.models import User
from .forms import LessonsForm

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView


@login_required(login_url='login')
def lessons(request):
    cid=request.GET['cid']
    course=Courses.objects.get(pk=cid)
    lessons=Lessons.objects.filter(course=course)
    context={'course':course,'lessons':lessons}		
    return render(request,'lessonsApp/lessons_list.html',context)


@login_required(login_url='login')

def createLesson(request):
	if request.method=='GET':
		if 'cid' in request.GET:
			cid=request.GET['cid']
			course=Courses.objects.get(pk=cid)
			form=LessonsForm()
			context={'course':course,'form':form}	
			return render(request,'lessonsApp/lessons_create.html',context)
		return HttpResponse(status=404)
			
	if request.method=='POST':
		if 'cid' in request.POST:
			cid=request.POST.get('cid')
			course=Courses.objects.get(pk=cid)
			form=LessonsForm(request.POST,request.FILES)
			if form.is_valid():
				lesson=form.save(commit=False)
				lesson.course=course
				lesson.save()
				return redirect('/lessons/?cid='+cid)				
		return HttpResponse(status=400)	

@method_decorator(login_required(login_url='/users/'), name='dispatch')	
class LessonsUpdateView(UpdateView):

	model=Lessons
	form_class=LessonsForm
	template_name_suffix = '_update_form'
	success_url='/'

	def get_object(self):
		id=self.kwargs.get("id")
		cid=self.kwargs.get("cid")
		self.success_url='/lessons/?cid='+str(cid)
		return get_object_or_404(Lessons,id=id)		

@method_decorator(login_required(login_url='/users/'), name='dispatch')
class LessonsDeleteView(DeleteView):
	model=Lessons
	template_name_suffix = '_delete'
	success_url='/'

	def get_object(self):
		id=self.kwargs.get("id")
		cid=self.kwargs.get("cid")
		self.success_url='/lessons/?cid='+str(cid)
		return get_object_or_404(Lessons,id=id)
