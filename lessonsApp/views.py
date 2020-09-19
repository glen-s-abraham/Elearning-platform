from django.shortcuts import render
from lessonsApp.models import Lessons
from coursesApp.models import Courses
from django.contrib.auth.models import User
from .forms import LessonsForm
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def lessons(request):
    user=request.user
    courses=Courses.objects.filter(author=user)
    lessons=None

    if request.method=='GET':
    	if 'Find' in request.GET:
    		cid=None
    		cid=request.GET['course']
    		print(cid)
    		if cid:
    			course=Courses.objects.get(pk=cid)
    			lessons=Lessons.objects.filter(course=course)
    context={'courses':courses,'lessons':lessons}			
    return render(request,'lessons.html',context)

@login_required(login_url='login')
def createLesson(request):
	user=request.user
	courses=Courses.objects.filter(author=user)
	form=LessonsForm()
	cid=None
	course=None
	if request.method=='GET':
		if 'Select' in request.GET:
			cid=cid=request.GET['course']
			if cid:
				print(cid)
				course=Courses.objects.get(pk=cid)
				if course:
					print(course)
	if request.method=='POST':
		if 'Add' in request.POST:
			print(request.FILES)
			cid=request.POST['cid']
			if cid:
				print(cid)
				course=Courses.objects.get(pk=cid)
				if course:
					form=LessonsForm(request.POST,request.FILES)
					if form.is_valid():
						lesson=form.save(commit=False)
						lesson.course=course
						lesson.save()






	context={'courses':courses,'form':form,'course':course}
	
	print(context)
	return render(request,'createLesson.html',context)
	
    

    
	
@login_required(login_url='login')
def updateLesson(request,id=-1):
	form=LessonsForm()
	lid=None
	if id>0:
		lesson=Lessons.objects.get(pk=id)
		print(lesson)
		form=LessonsForm(instance=lesson)
		lid=id;
	
	if request.method=='POST':
		if 'Update' in request.POST:
			id=request.POST['lid']
			if id:
				lesson=Lessons.objects.get(pk=id)
				course=lesson.course
				form=LessonsForm(request.POST,request.FILES,instance=lesson)
				if form.is_valid():
					lesson=form.save(commit=False)
					lesson.course=course
					lesson.save()
					print(lesson)
					print(request.FILES)

				
		
	context={'form':form}
	if lid:
		context['lid']=lid
	return render(request,'updateLesson.html',context)

@login_required(login_url='login')
def deleteLesson(request,id=-1):
	context={};
	if id>0:
		lesson=Lessons.objects.get(pk=id)
		print(lesson)
		if lesson:
			context['lesson']=lesson;

	if request.method=='POST':
		if 'Delete' in request.POST:
			id=request.POST['lid']
			if id:
				lesson=Lessons.objects.get(pk=id)
				lesson.delete()
	
	
	return render(request,'deleteLesson.html',context)		


