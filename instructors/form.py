from django import forms
from .models import Instructor


class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = '__all__'

        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome do Instrutor'}),
            'age': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'services': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Separe os serviços prestados por vírgula'}),
        }
