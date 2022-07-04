from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home-page"),
    path('cProgramming', views.cProgramming, name="c-programming-page"),
    path('python', views.python, name="python-page"),
    path('dsa', views.dsa, name="dsa-page"),
    path('oop', views.oop, name="oop-page"),
    path('androidApp', views.androidApp, name="androidApp-page"),
    path('webDev', views.webDev, name="webDev-page"),
    path('register', views.userRegistration, name="registration-page"),
    path('profileUpdate', views.userProfileUpdate, name="profile-update-page"),
    path('changePassword', views.userChangePassword, name="change-password-page"),
    path('login', views.userLogin, name="login-page"),
    path('logout', views.userLogout, name="logout-page")
]
