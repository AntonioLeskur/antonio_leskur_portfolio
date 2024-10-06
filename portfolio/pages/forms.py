from django import forms
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['your_email', 'title', 'message']
        widgets = {
            'your_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }