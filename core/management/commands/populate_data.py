"""
Management command to populate the database with sample data
"""
from django.core.management.base import BaseCommand
from core.models import Project, CompanyInfo, Testimonial


class Command(BaseCommand):
    help = 'Populate database with sample data for Srihari Developers'

    def handle(self, *args, **options):
        self.stdout.write("Populating database with sample data...")

        # Create company info
        company_info, created = CompanyInfo.objects.get_or_create(
            defaults={
                'name': 'Srihari Developers',
                'tagline': 'Building Dreams, Creating Realities',
                'description': 'Leading construction company in Tirupati specializing in residential and commercial projects.',
                'phone': '+91-9014376635',
                'email': 'info@sriharidevelopers.com',
                'address': 'VSM BUILDING, Renigunta Rd, Tirupati, Andhra Pradesh 517501',
                'established_year': 2015,
                'completed_projects': 50,
                'happy_clients': 200,
            }
        )
        if created:
            self.stdout.write("✓ Company info created")

        # Create sample projects
        projects = [
            {
                'title': 'Luxury Villa Complex',
                'description': 'Premium residential villas with modern amenities',
                'location': 'Tirupati',
                'area': '2500 sq ft',
                'status': 'completed',
                'featured': True,
                'category': 'residential'
            },
            {
                'title': 'Commercial Plaza',
                'description': 'Multi-story commercial building with retail spaces',
                'location': 'Renigunta Road',
                'area': '5000 sq ft', 
                'status': 'completed',
                'featured': True,
                'category': 'commercial'
            },
            {
                'title': 'Modern Apartments',
                'description': 'Contemporary apartment complex with all facilities',
                'location': 'Tirupati',
                'area': '1200 sq ft',
                'status': 'completed',
                'featured': True,
                'category': 'residential'
            }
        ]

        for project_data in projects:
            project, created = Project.objects.get_or_create(
                title=project_data['title'],
                defaults=project_data
            )
            if created:
                self.stdout.write(f"✓ Project '{project.title}' created")

        # Create sample testimonials
        testimonials = [
            {
                'client_name': 'Rajesh Kumar',
                'content': 'Excellent work quality and timely delivery. Highly recommended!',
                'rating': 5,
                'is_featured': True,
                'project_type': 'Villa Construction'
            },
            {
                'client_name': 'Priya Sharma', 
                'content': 'Professional team with great attention to detail.',
                'rating': 5,
                'is_featured': True,
                'project_type': 'Home Renovation'
            },
            {
                'client_name': 'Venkat Reddy',
                'content': 'Best construction company in Tirupati. Great experience!',
                'rating': 5,
                'is_featured': True,
                'project_type': 'Commercial Building'
            }
        ]

        for testimonial_data in testimonials:
            testimonial, created = Testimonial.objects.get_or_create(
                client_name=testimonial_data['client_name'],
                defaults=testimonial_data
            )
            if created:
                self.stdout.write(f"✓ Testimonial from '{testimonial.client_name}' created")

        self.stdout.write(
            self.style.SUCCESS("Database populated successfully! Your website should now work properly.")
        )