"""
Firebase Admin Setup for Srihari Developers

This module initializes Firebase Admin SDK for server-side operations
with Firestore database for storing projects, contacts, and other data.
"""

import firebase_admin
from firebase_admin import credentials, firestore
from django.conf import settings
import os
import logging

# Configure logging
logger = logging.getLogger(__name__)

# Global variables to store Firebase instances
_db = None
_app = None


def initialize_firebase():
    """
    Initialize Firebase Admin SDK
    
    Returns:
        firestore.Client: Firestore database client
    """
    global _db, _app
    
    if _app is None:
        try:
            # Check if service account key file exists
            if hasattr(settings, 'FIREBASE_SERVICE_ACCOUNT_KEY') and os.path.exists(settings.FIREBASE_SERVICE_ACCOUNT_KEY):
                # Initialize with service account key file
                cred = credentials.Certificate(settings.FIREBASE_SERVICE_ACCOUNT_KEY)
                _app = firebase_admin.initialize_app(cred)
                logger.info("Firebase initialized with service account key")
            else:
                # Initialize with default credentials (for deployment)
                _app = firebase_admin.initialize_app()
                logger.info("Firebase initialized with default credentials")
                
            _db = firestore.client()
            logger.info("Firestore client initialized successfully")
            
        except Exception as e:
            logger.error(f"Firebase initialization failed: {str(e)}")
            # For development without Firebase setup
            _db = None
            
    return _db


def get_firestore_client():
    """
    Get Firestore database client
    
    Returns:
        firestore.Client or None: Firestore client if available
    """
    if _db is None:
        return initialize_firebase()
    return _db


def is_firebase_available():
    """
    Check if Firebase is properly configured and available
    
    Returns:
        bool: True if Firebase is available, False otherwise
    """
    try:
        db = get_firestore_client()
        return db is not None
    except Exception:
        return False


# Initialize Firebase when the module is imported
try:
    initialize_firebase()
except Exception as e:
    logger.warning(f"Firebase initialization failed during import: {str(e)}")
    logger.warning("The website will work in local mode without Firebase features")