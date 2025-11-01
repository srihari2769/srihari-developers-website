"""
Firebase utilities for Srihari Developers website

This module provides helper functions for common Firebase operations
like CRUD operations for projects, contacts, and testimonials.
"""

from .firebase_admin_setup import get_firestore_client, is_firebase_available
from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class FirebaseService:
    """Service class for Firebase operations"""
    
    def __init__(self):
        self.db = get_firestore_client()
        
    def is_available(self):
        """Check if Firebase is available"""
        return is_firebase_available() and self.db is not None


class ProjectService(FirebaseService):
    """Service for project-related Firebase operations"""
    
    COLLECTION_NAME = 'projects'
    
    def get_all_projects(self):
        """
        Get all projects from Firestore
        
        Returns:
            list: List of project documents
        """
        if not self.is_available():
            return []
            
        try:
            projects = []
            docs = self.db.collection(self.COLLECTION_NAME).order_by('created_at', direction='DESCENDING').get()
            
            for doc in docs:
                project_data = doc.to_dict()
                project_data['id'] = doc.id
                projects.append(project_data)
                
            return projects
        except Exception as e:
            logger.error(f"Error fetching projects: {str(e)}")
            return []
    
    def get_featured_projects(self, limit=6):
        """
        Get featured projects for homepage
        
        Args:
            limit (int): Maximum number of projects to return
            
        Returns:
            list: List of featured project documents
        """
        if not self.is_available():
            return []
            
        try:
            projects = []
            docs = (self.db.collection(self.COLLECTION_NAME)
                   .where('featured', '==', True)
                   .order_by('created_at', direction='DESCENDING')
                   .limit(limit)
                   .get())
            
            for doc in docs:
                project_data = doc.to_dict()
                project_data['id'] = doc.id
                projects.append(project_data)
                
            return projects
        except Exception as e:
            logger.error(f"Error fetching featured projects: {str(e)}")
            return []
    
    def get_project_by_id(self, project_id):
        """
        Get a specific project by ID
        
        Args:
            project_id (str): Project document ID
            
        Returns:
            dict or None: Project data if found
        """
        if not self.is_available():
            return None
            
        try:
            doc = self.db.collection(self.COLLECTION_NAME).document(project_id).get()
            if doc.exists:
                project_data = doc.to_dict()
                project_data['id'] = doc.id
                return project_data
            return None
        except Exception as e:
            logger.error(f"Error fetching project {project_id}: {str(e)}")
            return None
    
    def create_project(self, project_data):
        """
        Create a new project
        
        Args:
            project_data (dict): Project information
            
        Returns:
            str or None: Document ID if successful
        """
        if not self.is_available():
            return None
            
        try:
            project_data['created_at'] = datetime.now()
            project_data['updated_at'] = datetime.now()
            
            doc_ref = self.db.collection(self.COLLECTION_NAME).add(project_data)
            logger.info(f"Project created with ID: {doc_ref[1].id}")
            return doc_ref[1].id
        except Exception as e:
            logger.error(f"Error creating project: {str(e)}")
            return None


class ContactService(FirebaseService):
    """Service for contact-related Firebase operations"""
    
    COLLECTION_NAME = 'contacts'
    
    def submit_contact(self, contact_data):
        """
        Submit a contact inquiry
        
        Args:
            contact_data (dict): Contact form data
            
        Returns:
            str or None: Document ID if successful
        """
        if not self.is_available():
            return None
            
        try:
            contact_data['created_at'] = datetime.now()
            contact_data['responded'] = False
            
            doc_ref = self.db.collection(self.COLLECTION_NAME).add(contact_data)
            logger.info(f"Contact inquiry submitted with ID: {doc_ref[1].id}")
            return doc_ref[1].id
        except Exception as e:
            logger.error(f"Error submitting contact: {str(e)}")
            return None
    
    def get_all_contacts(self):
        """
        Get all contact inquiries (admin use)
        
        Returns:
            list: List of contact documents
        """
        if not self.is_available():
            return []
            
        try:
            contacts = []
            docs = self.db.collection(self.COLLECTION_NAME).order_by('created_at', direction='DESCENDING').get()
            
            for doc in docs:
                contact_data = doc.to_dict()
                contact_data['id'] = doc.id
                contacts.append(contact_data)
                
            return contacts
        except Exception as e:
            logger.error(f"Error fetching contacts: {str(e)}")
            return []


class TestimonialService(FirebaseService):
    """Service for testimonial-related Firebase operations"""
    
    COLLECTION_NAME = 'testimonials'
    
    def get_featured_testimonials(self, limit=6):
        """
        Get featured testimonials for display
        
        Args:
            limit (int): Maximum number of testimonials to return
            
        Returns:
            list: List of testimonial documents
        """
        if not self.is_available():
            return []
            
        try:
            testimonials = []
            docs = (self.db.collection(self.COLLECTION_NAME)
                   .where('is_featured', '==', True)
                   .order_by('created_at', direction='DESCENDING')
                   .limit(limit)
                   .get())
            
            for doc in docs:
                testimonial_data = doc.to_dict()
                testimonial_data['id'] = doc.id
                testimonials.append(testimonial_data)
                
            return testimonials
        except Exception as e:
            logger.error(f"Error fetching testimonials: {str(e)}")
            return []
    
    def create_testimonial(self, testimonial_data):
        """
        Create a new testimonial
        
        Args:
            testimonial_data (dict): Testimonial information
            
        Returns:
            str or None: Document ID if successful
        """
        if not self.is_available():
            return None
            
        try:
            testimonial_data['created_at'] = datetime.now()
            
            doc_ref = self.db.collection(self.COLLECTION_NAME).add(testimonial_data)
            logger.info(f"Testimonial created with ID: {doc_ref[1].id}")
            return doc_ref[1].id
        except Exception as e:
            logger.error(f"Error creating testimonial: {str(e)}")
            return None


# Service instances
project_service = ProjectService()
contact_service = ContactService()
testimonial_service = TestimonialService()