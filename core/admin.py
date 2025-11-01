"""
Admin configuration for Srihari Developers core app
"""

from django.contrib import admin
from .models import Project, ProjectCategory, ContactInquiry, Testimonial, CompanyInfo


@admin.register(CompanyInfo)
class CompanyInfoAdmin(admin.ModelAdmin):
    list_display = ['company_name', 'phone', 'email', 'updated_at']
    fieldsets = (
        ('Basic Information', {
            'fields': ('company_name', 'tagline', 'description')
        }),
        ('Contact Details', {
            'fields': ('phone', 'email', 'address', 'website')
        }),
        ('Social Media', {
            'fields': ('facebook_url', 'instagram_url', 'linkedin_url', 'youtube_url'),
            'classes': ['collapse']
        }),
        ('Business Information', {
            'fields': ('established_year', 'license_number', 'logo_url'),
            'classes': ['collapse']
        }),
    )


@admin.register(ProjectCategory)
class ProjectCategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_at']
    search_fields = ['name']


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'status', 'category', 'featured', 'completion_date', 'created_at']
    list_filter = ['status', 'category', 'featured', 'created_at']
    search_fields = ['name', 'location', 'description']
    list_editable = ['status', 'featured']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'location', 'category', 'status')
        }),
        ('Project Details', {
            'fields': ('description', 'completion_date', 'image_url')
        }),
        ('Display Options', {
            'fields': ('featured',),
            'description': 'Control how this project appears on the website'
        }),
    )


@admin.register(ContactInquiry)
class ContactInquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'inquiry_type', 'created_at', 'responded']
    list_filter = ['inquiry_type', 'responded', 'created_at']
    search_fields = ['name', 'email', 'phone', 'message']
    list_editable = ['responded']
    readonly_fields = ['created_at']
    date_hierarchy = 'created_at'
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email', 'phone')
        }),
        ('Inquiry Details', {
            'fields': ('inquiry_type', 'message')
        }),
        ('Status', {
            'fields': ('responded', 'created_at')
        }),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ['client_name', 'project_name', 'rating', 'is_featured', 'created_at']
    list_filter = ['rating', 'is_featured', 'created_at']
    search_fields = ['client_name', 'project_name', 'testimonial_text']
    list_editable = ['is_featured', 'rating']
    
    fieldsets = (
        ('Client Information', {
            'fields': ('client_name', 'client_position', 'project_name', 'client_image')
        }),
        ('Testimonial', {
            'fields': ('testimonial_text', 'rating')
        }),
        ('Display Options', {
            'fields': ('is_featured',)
        }),
    )


# Customize admin site
admin.site.site_header = "Srihari Developers Admin"
admin.site.site_title = "Srihari Developers Admin Portal"
admin.site.index_title = "Welcome to Srihari Developers Administration"