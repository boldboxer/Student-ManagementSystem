from django import forms 
from .models import Student

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class StudentForm(forms.ModelForm):
  class Meta:
    model = Student
    fields = ['student_number', 'first_name', 'last_name', 'email', 'field_of_study', 'gpa']
    labels = {
      'student_number': 'Student Number', 
      'first_name': 'First Name', 
      'last_name': 'Last Name', 
      'email': 'Email', 
      'field_of_study': 'Field of Study', 
      'gpa': 'GPA'
    }
    widgets = {
      'student_number': forms.NumberInput(attrs={'class': 'form-control'}), 
      'first_name': forms.TextInput(attrs={'class': 'form-control'}),
      'last_name': forms.TextInput(attrs={'class': 'form-control'}),
      'email': forms.EmailInput(attrs={'class': 'form-control'}),
      'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
      'gpa': forms.NumberInput(attrs={'class': 'form-control'}),
    }

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user