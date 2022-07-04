from django.contrib.auth import update_session_auth_hash
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from elapp.form import MyUserChangeForm, MyPasswordChangeForm, MyUserCreationForm


# home
def home(request):
    if request.user.is_authenticated:
        return render(request, 'elapp/home.html')
    else:
        return redirect('/login')

# c programming
def cProgramming(request):
    if request.user.is_authenticated:
        return render(request, 'elapp/cProgramming.html')
    else:
        return redirect('/login')

# python bootcamp 2022
def python(request):
    if request.user.is_authenticated:
        return render(request, 'elapp/python.html')
    else:
        return redirect('/login')

# data structure & algorithms
def dsa(request):
    if request.user.is_authenticated:
        return render(request, 'elapp/dsa.html')
    else:
        return redirect('/login')

# object oriented programming using java/c++
def oop(request):
    if request.user.is_authenticated:
        return render(request, 'elapp/oop.html')
    else:
        return redirect('/login')

# android app development
def androidApp(request):
    if request.user.is_authenticated:
        return render(request, 'elapp/androidApp.html')
    else:
        return redirect('/login')

# web development
def webDev(request):
    if request.user.is_authenticated:
        return render(request, 'elapp/webDev.html')
    else:
        return redirect('/login')


# userRegistration
def userRegistration(request):
    if request.method == "POST":
        frm = MyUserCreationForm(request.POST)
        if frm.is_valid():
            frm.save()
            messages.success(request, 'User Registration Has Been Successfully Completed.')
            return redirect('/login')
    else:
        frm = MyUserCreationForm()
    return render(request, 'elapp/Registration.html', {'frm': frm})


# userProfileUpdate
def userProfileUpdate(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            frm = MyUserChangeForm(request.POST, instance=request.user)
            if frm.is_valid():
                frm.save()
                messages.success(request, 'Profile has been updated successfully.')
        else:
            frm = MyUserChangeForm(instance=request.user)
        return render(request, 'elapp/profileUpdate.html', {'frm': frm, 'f_name': request.user.first_name, 'l_name': request.user.last_name})
    else:
        return redirect('/Login')

# userChangePassword
def userChangePassword(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            frm = MyPasswordChangeForm(user=request.user, data=request.POST)
            if frm.is_valid():
                frm.save()
                update_session_auth_hash(request, frm.user)
                messages.success(request, 'Your password has been changed successfully.')
        else:
            frm = MyPasswordChangeForm(user=request.user)
        return render(request, 'elapp/changePassword.html', {'frm': frm, 'f_name': request.user.first_name, 'l_name': request.user.last_name})
    else:
        return redirect('/Login')

# userLogin
def userLogin(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Check your username and password !!!')
            return redirect('/login')
    else:
        return render(request, 'elapp/login.html')

# userLogout
def userLogout(request):
    auth.logout(request)
    return redirect('/')


