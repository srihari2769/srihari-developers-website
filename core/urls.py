"""
URL Configuration for core app
"""

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    # Main pages
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('projects/', views.projects, name='projects'),
    path('contact/', views.contact, name='contact'),
    
    # Project details
    path('project/<str:project_id>/', views.project_detail, name='project_detail'),
    
    # Form submissions
    path('service-inquiry/', views.service_inquiry, name='service_inquiry'),
    path('newsletter-subscribe/', views.newsletter_subscribe, name='newsletter_subscribe'),
    
    # API endpoints for AJAX calls
    path('api/projects/', views.api_projects, name='api_projects'),
    path('api/testimonials/', views.api_testimonials, name='api_testimonials'),
]