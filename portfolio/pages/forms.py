from django import forms
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = ['your_email', 'subject', 'message']
        widgets = {
            'your_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your Email'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message'}),
        }