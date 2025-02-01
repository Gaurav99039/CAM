from django.shortcuts import render
from .forms import CreateUserFrom
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.shortcuts import redirect
from django.contrib.auth.models import Group
# Create your views here.


def registration(request):
    form = CreateUserFrom()
    if request.method == 'POST':
        form = CreateUserFrom(request.POST)
        if form.is_valid():
            user = form.save()
            group = Group.objects.get(name='student')
            user.groups.add(group)
            messages.success(request,'Account was created for ' + form.cleaned_data.get('username'))
            return redirect('login')
    context = {'form':form}


    return render(request,'accounts/registration.html',context)


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('registration')
        else:
            messages.info(request,'Username or Password is incorrect')
    context = {}
    return render(request,'accounts/login.html',context)

def home(request):
    context = {}
    return render(request,'accounts/home.html',context)

