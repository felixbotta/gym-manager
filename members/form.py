from django import forms
from .models import Member


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = '__all__'

        widgets = {
            'url': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'https://'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'email:': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E-mail'}),
            'birth': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Peso'}),
            'height': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Altura'}),
        }
