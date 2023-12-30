# forms.py
from django import forms
from .models import CustomUser

class EditUsersForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name','password']  # Add more fields as needed

class AddUsersForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','email','password','first_name','last_name','age']
