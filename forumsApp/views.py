from django.shortcuts import get_object_or_404
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseNotFound
from forumsApp.models import Threads
from forumsApp.models import Replies
from forumsApp.forms import ThreadsForm
from forumsApp.forms import RepliesForm

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic.list import ListView 
from django.views.generic.detail import DetailView  
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView

@method_decorator(login_required(login_url='/users/'), name='dispatch')
class ThreadsView(ListView):
	template_name='forumsApp/threads_list'
	model=Threads


@method_decorator(login_required(login_url='/users/'), name='dispatch')
class MyThreadsView(ListView):
	model=Threads
	template_name='forumsApp/my_threads_list.html'
	def get_queryset(self):
		user=self.request.user
		queryset=Threads.objects.filter(author=user.id)
		return queryset


@method_decorator(login_required(login_url='/users/'), name='dispatch')	
class ThreadsCreateView(CreateView):
	model=Threads
	form_class=ThreadsForm
	success_url='/community/'

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)	

@method_decorator(login_required(login_url='/users/'), name='dispatch')	
class ThreadsUpdateView(UpdateView):

	model=Threads
	form_class=ThreadsForm
	success_url='/community/myThreads/'

	def get_object(self):
		id=self.kwargs.get("id")
		return get_object_or_404(Threads,id=id)



@method_decorator(login_required(login_url='/users/'), name='dispatch')
class ThreadsDeleteView(DeleteView):
	model=Threads
	template_name_suffix = '_delete'
	success_url='/community/myThreads/'

	def get_object(self):
		id=self.kwargs.get("id")
		return get_object_or_404(Threads,id=id)		


@login_required(login_url='login')
def replies(request):
	if request.method=='GET':
	    tid=request.GET.get('tid')
	    if tid:
	    	thread=get_object_or_404(Threads,pk=tid)
	    	replies=Replies.objects.filter(thread=thread)
	    	form=RepliesForm()
	    	context={'thread':thread,'replies':replies,'form':form}		
	    	return render(request,'forumsApp/replies_list.html',context)
	    return HttpResponseNotFound("Page not found")

	if request.method=='POST':
		if 'tid' in request.POST:
			tid=request.POST.get('tid')
			thread=get_object_or_404(Threads,pk=tid)
			form=RepliesForm(request.POST,request.FILES)
			if form.is_valid():
				lesson=form.save(commit=False)
				lesson.thread=thread
				lesson.author=request.user
				lesson.save()
				return redirect('/community/replies/?tid='+tid)				
		return HttpResponseNotFound("Page not found")	    	
	    
@method_decorator(login_required(login_url='/users/'), name='dispatch')
class RepliesDeleteView(DeleteView):
	model=Replies
	template_name = 'forumsApp/replies_delete.html'
	success_url='/'

	def get_object(self):
		rid=self.kwargs.get("rid")
		tid=self.kwargs.get("tid")
		self.success_url='/community/replies?tid='+str(tid)
		return get_object_or_404(Replies,id=rid)
	

 
	    
    
    
	    		
		    
	    