# init_db.py
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from app import app, db
from models import Candidate, Admin, Voter, Election, Vote, OTPVerification

def init_database():
    """Initialize the database with all tables"""
    with app.app_context():
        print("🛠️ Creating all tables...")
        
        # Drop all tables first if you want a fresh start (be careful in production!)
        # db.drop_all()
        
        # Create all tables
        db.create_all()
        
        print("✅ Database initialization successful.")
        print(f"📊 Database URI: {app.config['SQLALCHEMY_DATABASE_URI']}")

if __name__ == "__main__":
    init_database()

