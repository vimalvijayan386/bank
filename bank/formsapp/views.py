from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages,auth
from . forms import UserForm
from .models import Branch

# Create your views here.
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirm_password']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username exists")
                return redirect('register')
            user = User.objects.create_user(username=username, password=password)
            user.save();
            return redirect('login')
        else:
            messages.info(request, "password not matching")
    return render(request,"register.html")

def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password = request.POST['password']
        user=auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('details')
        else:
            messages.info(request,"invalid credintials")
            return redirect('login')

    return render(request,"login.html")

def details(request):

    return render(request,"details.html")

def add(request):
    if request.method == 'POST':

        return redirect('accepted')
    return render(request,"add.html")

def logout(request):

    return redirect ('/')

def accepted(request):
    return render(request,"accepted.html")

def user_form(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        return redirect('accepted')
        pass
    else:
        form = UserForm()
    return render(request, 'user_form.html', {'form': form})

def load_branches(request):
    district_id = request.GET.get('district')
    branches = Branch.objects.filter(district_id=district_id).order_by('name')
    return render(request, 'branch_dropdown_list_options.html', {'branches': branches})