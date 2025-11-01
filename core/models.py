"""
Models for Srihari Developers website

Since we're using Firebase for data storage, these models are primarily
for Django admin and local data management. The main data will be stored
in Firebase Firestore.
"""

from django.db import models
from django.core.validators import RegexValidator
from django.utils import timezone


class ProjectCategory(models.Model):
    """Categories for construction projects"""
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Project Categories"
        ordering = ['name']

    def __str__(self):
        return self.name


class Project(models.Model):
    """
    Local model for projects - mainly for Django admin.
    Main project data is stored in Firebase Firestore.
    """
    STATUS_CHOICES = [
        ('planning', 'Planning'),
        ('ongoing', 'Ongoing'),
        ('completed', 'Completed'),
        ('on_hold', 'On Hold'),
    ]

    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planning')
    description = models.TextField()
    image_url = models.URLField(blank=True, null=True)
    completion_date = models.DateField(blank=True, null=True)
    category = models.ForeignKey(ProjectCategory, on_delete=models.SET_NULL, null=True, blank=True)
    featured = models.BooleanField(default=False, help_text="Show on homepage")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.location}"


class ContactInquiry(models.Model):
    """
    Local model for contact inquiries - backup for Firebase data
    """
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{9,15}$',
        message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed."
    )
    phone = models.CharField(validators=[phone_regex], max_length=17)
    message = models.TextField()
    inquiry_type = models.CharField(
        max_length=50,
        choices=[
            ('general', 'General Inquiry'),
            ('project', 'Project Inquiry'),
            ('marketing', 'Marketing Services'),
            ('other', 'Other'),
        ],
        default='general'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    responded = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = "Contact Inquiries"
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.inquiry_type}"


class Testimonial(models.Model):
    """Customer testimonials"""
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100, blank=True)
    project_name = models.CharField(max_length=100, blank=True)
    testimonial_text = models.TextField()
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)], default=5)
    client_image = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.client_name} - {self.project_name}"


class CompanyInfo(models.Model):
    """Company information and settings"""
    company_name = models.CharField(max_length=200, default="Srihari Developers")
    tagline = models.CharField(max_length=300, default="Building Dreams, Creating Legacies")
    description = models.TextField()
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    address = models.TextField()
    website = models.URLField(blank=True)
    logo_url = models.URLField(blank=True)
    
    # Social Media
    facebook_url = models.URLField(blank=True)
    instagram_url = models.URLField(blank=True)
    linkedin_url = models.URLField(blank=True)
    youtube_url = models.URLField(blank=True)
    
    # Business Details
    established_year = models.IntegerField(blank=True, null=True)
    license_number = models.CharField(max_length=100, blank=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Company Information"
        verbose_name_plural = "Company Information"

    def __str__(self):
        return self.company_name

    def save(self, *args, **kwargs):
        # Ensure only one instance exists
        if not self.pk and CompanyInfo.objects.exists():
            raise ValueError("Only one CompanyInfo instance is allowed")
        super().save(*args, **kwargs)