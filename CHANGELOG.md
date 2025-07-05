# Changelog

All notable changes to the Smart Voting System will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Multi-language support planning
- Mobile app version planning
- Advanced analytics dashboard

## [1.0.0] - 2025-01-05

### Added
- **Core Voting System**
  - Complete voter registration with 3-step process
  - Email OTP verification system
  - Advanced face recognition authentication (51-frame capture)
  - Secure password hashing with bcrypt
  - Multi-factor authentication (Email + Face)

- **Admin Panel**
  - Complete admin dashboard
  - Election creation and management
  - Candidate management with photo uploads
  - Real-time results viewing
  - Voter management system
  - Data export functionality (CSV/PDF)

- **Security Features**
  - Face recognition using dlib and OpenCV
  - Session management with Flask sessions
  - XSS and injection prevention
  - Rate limiting for failed attempts
  - Secure file upload handling

- **User Interface**
  - Modern glass morphism design
  - Responsive mobile-first layout
  - Animated backgrounds and transitions
  - Real-time progress indicators
  - Live camera feed for face registration

- **Database System**
  - SQLite database with SQLAlchemy ORM
  - Proper relationships between tables
  - Migration support with Flask-Migrate
  - Data integrity constraints

### Technical Specifications
- **Backend**: Flask 3.1.1
- **Database**: SQLAlchemy with SQLite
- **Face Recognition**: face_recognition 1.3.0 with dlib
- **Computer Vision**: OpenCV 4.11.0
- **Email**: Flask-Mail with Gmail SMTP
- **Security**: bcrypt password hashing
- **Frontend**: Modern HTML5/CSS3/JavaScript

### Database Schema
- **Voter Table**: User registration and authentication
- **Admin Table**: Administrator accounts
- **Election Table**: Election management
- **Candidate Table**: Candidate information
- **Vote Table**: Voting records
- **OTPVerification Table**: Email verification

### Security Measures
- Password hashing with bcrypt and salt
- Face encoding encryption and secure storage
- OTP expiration and single-use verification
- Session timeout and security
- Input validation and sanitization

### API Endpoints
- `/api/start-face-scan` - Initialize face scanning
- `/api/process-face-frame` - Process face frames
- `/register/step1` - Email and password registration
- `/register/step2` - OTP verification
- `/register/step3` - Face registration
- `/admin-dashboard` - Admin panel access
- `/vote` - Voting functionality

### Known Issues
- Face recognition may require good lighting
- Camera permissions needed for registration
- Email delivery depends on SMTP configuration

### Performance
- Face registration: ~10-15 seconds for 51 frames
- Face verification: ~2-3 seconds average
- Database queries optimized for small to medium scale
- Responsive design tested on multiple devices

## [0.9.0] - 2024-12-15

### Added
- Initial project setup
- Basic Flask application structure
- Database models creation
- Email configuration setup

### Security
- Basic password hashing implementation
- Session management setup

## [0.8.0] - 2024-12-01

### Added
- Project planning and architecture
- Technology stack selection
- Initial repository setup

---

## Version Numbering

This project uses [Semantic Versioning](https://semver.org/):
- **MAJOR** version for incompatible API changes
- **MINOR** version for backwards-compatible functionality additions  
- **PATCH** version for backwards-compatible bug fixes

## Contributing

Please read [CONTRIBUTING.md](CONTRIBUTING.md) for details on our code of conduct and the process for submitting pull requests.

## Authors

- **Sukesh Kumar** - *Initial development* - sukesh2294@gmail.com
- **Sudhanshu Kumar** - *Co-developer* - sudhanshujii78@gmail.com
