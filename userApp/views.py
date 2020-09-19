from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.forms import AuthenticationForm

def login_request(request):
	if request.method=='POST':
		username=request.POST['username']
		password=request.POST['password']
		print(username,password)
		user=authenticate(request,username=username,password=password)
		if user:
			login(request, user)
			print(user)
			return redirect('courses')
		else:
			print('no user')
			


	form=AuthenticationForm()
	return render(request=request,template_name='login.html',context={'form':form})

	

	
                 

def logout_request(request):
	logout(request)
	return redirect("login")

	
    
	
