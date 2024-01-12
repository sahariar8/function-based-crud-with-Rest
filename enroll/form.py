from django import forms
from .models import StudentRegistration
from django.core import validators

class StudentForm(forms.ModelForm):
    class Meta:
        model = StudentRegistration
        fields = ['name','email','password']
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(render_value=True,attrs={'class':'form-control'}),
        }
