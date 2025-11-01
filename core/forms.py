"""
Forms for Srihari Developers website
"""

from django import forms
from django.core.validators import RegexValidator
from .models import ContactInquiry


class ContactForm(forms.Form):
    """Contact form for customer inquiries"""
    
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Full Name',
            'required': True
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'your.email@example.com',
            'required': True
        })
    )
    
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    
    phone = forms.CharField(
        validators=[phone_regex],
        max_length=17,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': '+91 9999999999',
            'required': True
        })
    )
    
    inquiry_type = forms.ChoiceField(
        choices=[
            ('general', 'General Inquiry'),
            ('project', 'Project Inquiry'),
            ('marketing', 'Marketing Services'),
            ('investment', 'Investment Opportunity'),
            ('other', 'Other'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-control'
        }),
        initial='general'
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Tell us about your requirements...',
            'rows': 5,
            'required': True
        })
    )

    def clean_name(self):
        name = self.cleaned_data['name']
        if len(name) < 2:
            raise forms.ValidationError("Name must be at least 2 characters long.")
        return name

    def clean_message(self):
        message = self.cleaned_data['message']
        if len(message) < 10:
            raise forms.ValidationError("Please provide a more detailed message (at least 10 characters).")
        return message


class ServiceInquiryForm(forms.Form):
    """Service-specific inquiry form"""
    
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name'
        })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Email'
        })
    )
    
    phone = forms.CharField(
        max_length=15,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Phone Number'
        })
    )
    
    service_type = forms.ChoiceField(
        choices=[
            ('construction', 'Construction Services'),
            ('marketing', 'Project Marketing'),
            ('consultation', 'Real Estate Consultation'),
            ('investment', 'Investment Advisory'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    project_budget = forms.ChoiceField(
        choices=[
            ('10-25', '₹10L - ₹25L'),
            ('25-50', '₹25L - ₹50L'),
            ('50-1cr', '₹50L - ₹1Cr'),
            ('1cr+', '₹1Cr+'),
            ('not_decided', 'Not Decided Yet'),
        ],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    timeline = forms.ChoiceField(
        choices=[
            ('immediate', 'Immediate (Within 1 month)'),
            ('3months', 'Within 3 months'),
            ('6months', 'Within 6 months'),
            ('1year', 'Within 1 year'),
            ('flexible', 'Flexible timeline'),
        ],
        required=False,
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'Describe your requirements in detail...',
            'rows': 4
        }),
        required=False
    )


class NewsletterSubscriptionForm(forms.Form):
    """Newsletter subscription form"""
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your email address'
        })
    )
    
    name = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Your Name (Optional)'
        })
    )
    
    interests = forms.MultipleChoiceField(
        choices=[
            ('residential', 'Residential Projects'),
            ('commercial', 'Commercial Projects'),
            ('investment', 'Investment Opportunities'),
            ('market_updates', 'Market Updates'),
        ],
        widget=forms.CheckboxSelectMultiple(attrs={
            'class': 'form-check-input'
        }),
        required=False
    )