from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm, forms

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'placeholder': 'Username', 'class': 'form-control'}))
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={'placeholder': 'Last Name', 'class': 'form-control'}))
    email = forms.CharField(label='Email Address', widget=forms.EmailInput(
        attrs={'placeholder': 'Email-ID', 'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Password', 'class': 'form-control'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirm Password', 'class': 'form-control'}))
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]

class MyAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Username', 'class': 'form-control'}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Password', 'class': 'form-control'}))

class MyUserChangeForm(UserChangeForm):
    first_name = forms.CharField(label='First Name', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your First Name', 'class': 'form-control'}))
    last_name = forms.CharField(label='Last Name', widget=forms.TextInput(
        attrs={'placeholder': 'Enter Your Last Name', 'class': 'form-control'}))
    email = forms.CharField(label='Email Address', widget=forms.EmailInput(
        attrs={'placeholder': 'Enter Your Email-ID', 'class': 'form-control'}))
    password = None
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]

class MyPasswordChangeForm(PasswordChangeForm):
    old_password = forms.CharField(label='Current Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Current Password', 'class': 'form-control'}))
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter New Password', 'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(
        attrs={'placeholder': 'Enter Confirm Password', 'class': 'form-control'}))
