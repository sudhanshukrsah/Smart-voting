import os
from datetime import timedelta

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'Topsecreate'
    
    # Database Configuration
    # Use PostgreSQL if DATABASE_URL is provided (production/Render)
    # Otherwise use SQLite for local development
    DATABASE_URL = os.environ.get('DATABASE_URL')
    if DATABASE_URL:
        # Fix for Heroku/Render postgres:// to postgresql://
        if DATABASE_URL.startswith('postgres://'):
            DATABASE_URL = DATABASE_URL.replace('postgres://', 'postgresql://', 1)
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
        print("🐘 Using PostgreSQL database")
    else:
        # Local development with SQLite
        SQLALCHEMY_DATABASE_URI = 'sqlite:///voters.db'
        print("📁 Using SQLite database for local development")
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Email Configuration
    MAIL_SERVER = os.environ.get('MAIL_SERVER') or 'smtp.gmail.com'
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'True').lower() in ['true', '1', 'yes']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME') or 'smartvoting.verify@gmail.com'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD') or 'tdgpjvdyclmiyzss'
    
    # Session Configuration
    PERMANENT_SESSION_LIFETIME = timedelta(minutes=30)
    
    # Upload Configuration
    UPLOAD_FOLDER = 'static/uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
