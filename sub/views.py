from django.shortcuts import render

# Create your views here.
def assignment_page(request):
    return render(request,'assignment.html')


def instructor(request):

    return render(request,'instructor.html')


from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login ,logout
from django.contrib import messages
from . models import User

# Create your views here.
def log_out(request):
    logout(request)
    return redirect('index')



def user_page(request):
    context={}
    if request.POST and 'register' in request.POST:
        context['register']=True
        try:
            username=request.POST.get('username')
            email=request.POST.get('email')
            password1=request.POST.get('password1')
            password2=request.POST.get('password2')
            role = request.POST.get('role')

            if password1 != password2:
                messages.error(request, "Passwords do not match!")
            elif User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists!")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email is already registered!")
            else:
                user = User.objects.create_user(
                username=username, 
                email=email, 
                password=password1,
                role=role  # Save role
            )
                success_message='registed succesfully'
                messages.success(request,success_message)
        except Exception as e:
            error_message='duplicate name or invalid inputs'
            messages.error(request,error_message)

    if request.POST and 'login' in request.POST:
        context['register'] = False
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
    
        if user is not None:  # Authenticate successful
            login(request, user)
            messages.success(request, "Login successful!")
            if user.role == 'student':
                return redirect('index')  # Replace with your student home page URL name
            elif user.role == 'teacher':
                return redirect('index')  # Replace with your teacher home page URL name
            

        else:
            messages.error(request, "Invalid credentials!")    
      

    return render(request,'user.html',context)