from django.shortcuts import render
from django.shortcuts import get_object_or_404
from coursesApp.models import Courses
from .forms import CoursesForm
from django.contrib.auth.models import User
from .models import Courses
from django.contrib.auth.decorators import login_required

#CRUD Functionality for Courses
@login_required(login_url='login')
def courses(request):
	user=request.user
	courses=Courses.objects.filter(author=user)
	return render(request,'courses.html',{'courses':courses})

@login_required(login_url='login')
def createCourse(request):
	isCreated=False;
	form = CoursesForm()
	user=request.user
	course=Courses
	if request.method == 'POST':
		print(request.POST)
		form = CoursesForm(request.POST)		
		if form.is_valid():
			course=form.save(commit=False)
			course.author=user
			course.save()
			isCreated=True		
			
	context={'form': form,'isCreated':isCreated}
	return render(request, 'createCourse.html',context )

@login_required(login_url='login')	
def updateCourse(request):
	user=request.user
	courseslist=Courses.objects.filter(author=user)
	form=CoursesForm()
	id=None
	if request.method=='GET':
		if 'Course' in request.GET:
			id=request.GET['course']
			if id:
				instance=Courses.objects.get(pk=id)
				if instance:
					form=CoursesForm(instance=instance)
	context={'courseslist':courseslist,'form':form}	
	if id:
		context['id']=id		
	if request.method=='POST':
		cid=None
		cid=request.POST['courseid'];
		if cid:
			print(cid)
			instance=Courses.objects.get(pk=cid)
			if instance:
					print(instance)
					user=request.user
					form = CoursesForm(request.POST,instance=instance)
					if form.is_valid():
						instance=form.save(commit=False)
						instance.author=user
						instance.save()
				
			
				
		
	
	return render(request, 'updateCourse.html',context)

@login_required(login_url='login')
def deleteCourse(request):
	user=request.user
	courseslist=Courses.objects.filter(author=user)
	context={'courseslist':courseslist}	
	form=CoursesForm()
	if request.method=='POST':
		id=request.POST['course'];
		if id:
			print(id)
			instance=Courses.objects.get(pk=id)
			if instance:
				print(instance)
				if 'Delete' in request.POST:
						
					print('deleting',instance)
					instance.delete()
	
	return render(request, 'deleteCourse.html',context)






    
    
   
	


			


