from django import forms
from .models import ClientApplication, ContactMessage

class ClientApplicationForm(forms.ModelForm):
    class Meta:
        model = ClientApplication
        fields = ['full_name', 'email', 'phone', 'company_name', 
                  'service_type', 'project_description', 'budget_range', 'timeline']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Full Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Company Name (Optional)'}),
            'service_type': forms.Select(attrs={'class': 'form-control'}),
            'project_description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Describe your project requirements'}),
            'budget_range': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Estimated budget range'}),
            'timeline': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Expected timeline'}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your Name'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Subject'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Your Message'}),
        }
