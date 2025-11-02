"""
Views for Srihari Developers website

This module contains all view functions that handle HTTP requests,
integrate with Firebase for dynamic content, and render templates.
"""

from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.core.paginator import Paginator
from django.urls import reverse
from django.conf import settings
import json
import logging

from .forms import ContactForm, ServiceInquiryForm, NewsletterSubscriptionForm
from .models import Project, ContactInquiry, Testimonial, CompanyInfo

# Firebase integration (disable for Vercel deployment)
try:
    from firebase_config.utils import project_service, contact_service, testimonial_service
    FIREBASE_AVAILABLE = True
except ImportError:
    FIREBASE_AVAILABLE = False
    project_service = None
    contact_service = None
    testimonial_service = None

logger = logging.getLogger(__name__)


def home(request):
    """
    Homepage view with featured projects and testimonials - works with empty database
    """
    logger.info("Homepage view called")
    
    # Start with safe defaults
    context = {
        'featured_projects': [],
        'testimonials': [],
        'company_info': {
            'company_name': 'Srihari Developers',
            'tagline': 'Building Dreams, Creating Realities',
            'description': 'Leading construction company in Tirupati specializing in residential and commercial projects.',
            'phone': '+91-9014376635',
            'email': 'info@sriharidevelopers.com',
            'address': 'VSM BUILDING, Renigunta Rd, Tirupati, Andhra Pradesh 517501'
        }
    }
    
    try:
        # Try to get company info from database
        company_info = CompanyInfo.objects.first()
        if company_info:
            context['company_info'] = company_info
            logger.info("Company info loaded from database")
        else:
            logger.info("Using default company info")
        
        # Try to get projects
        projects = Project.objects.filter(featured=True)[:6]
        context['featured_projects'] = list(projects)
        logger.info(f"Loaded {len(context['featured_projects'])} projects")
        
        # Try to get testimonials
        testimonials = Testimonial.objects.filter(is_featured=True)[:6]
        context['testimonials'] = list(testimonials)
        logger.info(f"Loaded {len(context['testimonials'])} testimonials")
            
    except Exception as e:
        logger.error(f"Error in homepage view: {str(e)}", exc_info=True)
        # Context already has safe defaults
    
    logger.info("Rendering home.html template")
    return render(request, 'home.html', context)


def about(request):
    """About page view"""
    context = {
        'company_info': None,
    }
    
    try:
        context['company_info'] = CompanyInfo.objects.first()
    except Exception as e:
        logger.error(f"Error loading company info: {str(e)}")
    
    return render(request, 'about.html', context)


def services(request):
    """Services page view"""
    context = {
        'service_form': ServiceInquiryForm(),
        'company_info': None,
    }
    
    try:
        context['company_info'] = CompanyInfo.objects.first()
    except Exception as e:
        logger.error(f"Error loading company info: {str(e)}")
    
    return render(request, 'services.html', context)


def projects(request):
    """
    Projects page view with pagination and filtering
    """
    context = {
        'projects': [],
        'project_categories': [],
        'total_projects': 0,
    }
    
    try:
        # Get all projects from Firebase
        all_projects = project_service.get_all_projects()
        
        if all_projects:
            context['projects'] = all_projects
            context['total_projects'] = len(all_projects)
        else:
            # Fallback to Django model
            django_projects = Project.objects.all().order_by('-created_at')
            context['projects'] = django_projects
            context['total_projects'] = django_projects.count()
            
        # Get project categories (from Django model)
        from .models import ProjectCategory
        context['project_categories'] = ProjectCategory.objects.all()
        
    except Exception as e:
        logger.error(f"Error loading projects: {str(e)}")
        # Fallback to Django model
        django_projects = Project.objects.all().order_by('-created_at')
        context['projects'] = django_projects
        context['total_projects'] = django_projects.count()
    
    return render(request, 'projects.html', context)


def project_detail(request, project_id):
    """
    Individual project detail view
    """
    context = {
        'project': None,
        'related_projects': [],
    }
    
    try:
        # Get project from Firebase
        project = project_service.get_project_by_id(project_id)
        
        if project:
            context['project'] = project
            # Get related projects
            related_projects = project_service.get_featured_projects(limit=4)
            # Remove current project from related projects
            context['related_projects'] = [p for p in related_projects if p.get('id') != project_id]
        else:
            # Try Django model as fallback
            try:
                django_project = Project.objects.get(id=project_id)
                context['project'] = {
                    'id': django_project.id,
                    'name': django_project.name,
                    'location': django_project.location,
                    'status': django_project.status,
                    'description': django_project.description,
                    'image_url': django_project.image_url,
                    'completion_date': django_project.completion_date,
                }
                context['related_projects'] = Project.objects.filter(featured=True).exclude(id=project_id)[:4]
            except Project.DoesNotExist:
                messages.error(request, "Project not found.")
                return redirect('core:projects')
                
    except Exception as e:
        logger.error(f"Error loading project {project_id}: {str(e)}")
        messages.error(request, "Error loading project details.")
        return redirect('core:projects')
    
    return render(request, 'project_detail.html', context)


def contact(request):
    """
    Contact page view with form handling
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            try:
                # Prepare data for Firebase
                contact_data = {
                    'name': form.cleaned_data['name'],
                    'email': form.cleaned_data['email'],
                    'phone': form.cleaned_data['phone'],
                    'inquiry_type': form.cleaned_data['inquiry_type'],
                    'message': form.cleaned_data['message'],
                }
                
                # Save to Firebase
                firebase_success = contact_service.submit_contact(contact_data)
                
                # Also save to Django model as backup
                try:
                    contact_inquiry = ContactInquiry.objects.create(
                        name=contact_data['name'],
                        email=contact_data['email'],
                        phone=contact_data['phone'],
                        inquiry_type=contact_data['inquiry_type'],
                        message=contact_data['message'],
                    )
                except Exception as e:
                    logger.warning(f"Failed to save contact to Django model: {str(e)}")
                
                if firebase_success:
                    messages.success(request, 
                        "Thank you for your inquiry! We'll get back to you within 24 hours.")
                else:
                    messages.success(request, 
                        "Your message has been received. We'll contact you soon!")
                
                return redirect('core:contact')
                
            except Exception as e:
                logger.error(f"Error submitting contact form: {str(e)}")
                messages.error(request, 
                    "There was an error submitting your form. Please try again or call us directly.")
        else:
            messages.error(request, "Please correct the errors below and try again.")
    else:
        form = ContactForm()
    
    context = {
        'form': form,
        'company_info': None,
    }
    
    try:
        context['company_info'] = CompanyInfo.objects.first()
    except Exception as e:
        logger.error(f"Error loading company info: {str(e)}")
    
    return render(request, 'contact.html', context)


@require_http_methods(["POST"])
def service_inquiry(request):
    """
    Handle service inquiry form submission via AJAX
    """
    if request.method == 'POST':
        form = ServiceInquiryForm(request.POST)
        if form.is_valid():
            try:
                # Prepare data for Firebase
                inquiry_data = {
                    'name': form.cleaned_data['name'],
                    'email': form.cleaned_data['email'],
                    'phone': form.cleaned_data['phone'],
                    'service_type': form.cleaned_data['service_type'],
                    'project_budget': form.cleaned_data.get('project_budget', ''),
                    'timeline': form.cleaned_data.get('timeline', ''),
                    'message': form.cleaned_data.get('message', ''),
                    'inquiry_type': 'service',
                }
                
                # Save to Firebase
                firebase_success = contact_service.submit_contact(inquiry_data)
                
                if firebase_success:
                    return JsonResponse({
                        'success': True,
                        'message': 'Service inquiry submitted successfully! We\'ll contact you soon.'
                    })
                else:
                    return JsonResponse({
                        'success': True,
                        'message': 'Your inquiry has been received. We\'ll get back to you soon!'
                    })
                    
            except Exception as e:
                logger.error(f"Error submitting service inquiry: {str(e)}")
                return JsonResponse({
                    'success': False,
                    'message': 'There was an error submitting your inquiry. Please try again.'
                })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all required fields correctly.',
                'errors': form.errors
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


@require_http_methods(["POST"])
def newsletter_subscribe(request):
    """
    Handle newsletter subscription
    """
    if request.method == 'POST':
        form = NewsletterSubscriptionForm(request.POST)
        if form.is_valid():
            try:
                subscription_data = {
                    'email': form.cleaned_data['email'],
                    'name': form.cleaned_data.get('name', ''),
                    'interests': form.cleaned_data.get('interests', []),
                    'subscription_type': 'newsletter',
                }
                
                # In a real implementation, you would save this to a newsletter service
                # For now, we'll save it as a contact inquiry
                newsletter_inquiry = contact_service.submit_contact({
                    'name': subscription_data['name'] or 'Newsletter Subscriber',
                    'email': subscription_data['email'],
                    'phone': 'Not provided',
                    'inquiry_type': 'newsletter',
                    'message': f"Newsletter subscription - Interests: {', '.join(subscription_data['interests'])}",
                })
                
                return JsonResponse({
                    'success': True,
                    'message': 'Successfully subscribed to our newsletter!'
                })
                
            except Exception as e:
                logger.error(f"Error processing newsletter subscription: {str(e)}")
                return JsonResponse({
                    'success': False,
                    'message': 'There was an error processing your subscription. Please try again.'
                })
        else:
            return JsonResponse({
                'success': False,
                'message': 'Please provide a valid email address.',
                'errors': form.errors
            })
    
    return JsonResponse({'success': False, 'message': 'Invalid request method.'})


def api_projects(request):
    """
    API endpoint to fetch projects data (for AJAX requests)
    """
    try:
        projects = project_service.get_all_projects()
        
        if not projects:
            # Fallback to Django model
            django_projects = Project.objects.all()
            projects = []
            for project in django_projects:
                projects.append({
                    'id': project.id,
                    'name': project.name,
                    'location': project.location,
                    'status': project.status,
                    'description': project.description,
                    'image_url': project.image_url or '',
                    'completion_date': project.completion_date.isoformat() if project.completion_date else None,
                    'featured': project.featured,
                })
        
        return JsonResponse({
            'success': True,
            'projects': projects
        })
        
    except Exception as e:
        logger.error(f"Error fetching projects via API: {str(e)}")
        return JsonResponse({
            'success': False,
            'message': 'Error fetching projects data.'
        })


def api_testimonials(request):
    """
    API endpoint to fetch testimonials data (for AJAX requests)
    """
    try:
        testimonials = testimonial_service.get_featured_testimonials()
        
        if not testimonials:
            # Fallback to Django model
            django_testimonials = Testimonial.objects.filter(is_featured=True)
            testimonials = []
            for testimonial in django_testimonials:
                testimonials.append({
                    'id': testimonial.id,
                    'client_name': testimonial.client_name,
                    'client_position': testimonial.client_position,
                    'project_name': testimonial.project_name,
                    'testimonial_text': testimonial.testimonial_text,
                    'rating': testimonial.rating,
                    'client_image': testimonial.client_image or '',
                })
        
        return JsonResponse({
            'success': True,
            'testimonials': testimonials
        })
        
    except Exception as e:
        logger.error(f"Error fetching testimonials via API: {str(e)}")
        return JsonResponse({
            'success': False,
            'message': 'Error fetching testimonials data.'
        })