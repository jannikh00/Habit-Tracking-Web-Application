from django import forms
from .models import Habit, Progress
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name', 'description', 'frequency']

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = ['date', 'status']  # Include fields for date and completion status
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.CheckboxInput(),
        }