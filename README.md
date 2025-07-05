# 🗳️ Smart Voting System

A secure, modern web-based voting application with **facial recognition authentication** and **OTP verification** built with Flask and advanced security features.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-3.1.1-green.svg)
![OpenCV](https://img.shields.io/badge/OpenCV-4.11.0-red.svg)
![Face Recognition](https://img.shields.io/badge/Face_Recognition-1.3.0-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🌟 Features

### 🔐 Security Features
- **Multi-factor Authentication**: Email OTP + Facial Recognition
- **Face Recognition**: Advanced facial encoding using dlib
- **Password Hashing**: bcrypt encryption for secure password storage
- **Session Management**: Secure session handling with Flask

### 👤 User Management
- **Voter Registration**: 3-step registration process with face capture
- **Admin Panel**: Complete admin dashboard for election management
- **Profile Management**: User profile with face verification

### 🗳️ Voting System
- **Dynamic Elections**: Create and manage multiple elections
- **Candidate Management**: Add candidates with photos and symbols
- **Real-time Results**: Live vote counting and results display
- **Vote Validation**: Prevent duplicate voting with multiple checks

### 📊 Data Management
- **Export Functionality**: Download voting data in CSV/PDF formats
- **Voter Lists**: Manage and view registered voters
- **Election Analytics**: Comprehensive voting statistics

## 🚀 Quick Start

### Prerequisites

Make sure you have Python 3.8+ installed on your system.

```bash
python --version
```

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/sudhanshukrsah/Smart-voting.git
cd smart-voting-system
```

2. **Create virtual environment**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Configure environment variables**

Create a `.env` file in the root directory:

```env
# Email Configuration (Gmail)
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password

# Database Configuration
DATABASE_URL=sqlite:///instance/voters.db

# Security
SECRET_KEY=your-secret-key-here
```

5. **Run the application**
```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## 🏗️ Project Structure

```
smart-voting-system/
├── app.py                 # Main Flask application
├── models.py             # Database models
├── config.py             # Configuration settings
├── init_db.py           # Database initialization
├── requirements.txt      # Python dependencies
├── instance/
│   └── voters.db        # SQLite database
├── static/
│   └── uploads/
│       ├── candidate_photos/  # Candidate images
│       └── symbols/          # Party symbols
├── templates/            # HTML templates
│   ├── index.html
│   ├── register_step1.html
│   ├── register_step2.html
│   ├── register_step3.html
│   ├── admin_dashboard.html
│   └── ... (other templates)
└── data/                # Face recognition data
```

## 👥 User Roles & Access

### 🔑 Admin Accounts

| Name | Email | Password | Role |
|------|-------|----------|------|
| Sukesh Kumar | s********@gmail.com | ********** | Admin-1 |
| Sudhanshu Kumar | s*********@gmail.com | ******** | Admin-2 |

### 🗳️ Voter Registration Flow

1. **Step 1**: Enter personal details and email
2. **Step 2**: OTP verification via email
3. **Step 3**: Face registration (51 frames capture)
4. **Step 4**: Account verification and login

## 🔧 Configuration

### Email Setup (Gmail)

1. Enable 2-factor authentication in Gmail
2. Generate app-specific password
3. Use the app password in `.env` file

### Database Setup

The application uses SQLite by default. For production, you can configure PostgreSQL or MySQL:

```python
# config.py
class Config:
    # For PostgreSQL
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/dbname'
    
    # For MySQL
    SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/dbname'
```

## 🔐 API Endpoints

### Authentication

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/start-face-scan` | Initialize face scanning |
| POST | `/api/process-face-frame` | Process face frame data |
| POST | `/register/step1` | Email and password setup |
| POST | `/register/step2` | OTP verification |

### Admin

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/admin-dashboard` | Admin dashboard |
| POST | `/admin/create-election` | Create new election |
| POST | `/admin/add-candidate` | Add election candidate |
| GET | `/admin/results` | View election results |

### Voting

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/voter-dashboard` | Voter dashboard |
| POST | `/vote` | Cast vote |
| GET | `/voter/results` | View results |

## 🎨 Frontend Features

### Modern UI/UX
- **Glass Morphism Design**: Modern glassmorphic interface
- **Responsive Layout**: Mobile-first responsive design
- **Animated Backgrounds**: Dynamic visual effects
- **Progress Indicators**: Real-time progress tracking
- **Loading States**: Smooth loading animations

### Face Recognition Interface
- **Live Camera Feed**: Real-time video preview
- **Face Detection Overlay**: Visual face tracking
- **Progress Tracking**: Frame capture progress
- **Status Indicators**: Clear feedback for users

## 🔒 Security Measures

### Data Protection
- **Password Hashing**: bcrypt with salt
- **Face Data Encryption**: Secure facial encoding storage
- **Session Security**: Secure session management
- **Input Validation**: XSS and injection prevention

### Authentication Security
- **Multi-factor Authentication**: Email + Face verification
- **OTP Expiration**: Time-limited OTP codes
- **Failed Attempt Handling**: Rate limiting protection
- **Session Timeout**: Automatic session expiration

## 🧪 Testing

### Manual Testing

1. **Registration Flow**
```bash
# Test voter registration
1. Navigate to registration page
2. Enter valid email and password
3. Verify OTP code
4. Complete face registration
```

2. **Admin Functions**
```bash
# Test admin operations
1. Login as admin
2. Create election
3. Add candidates
4. View results
```

### Face Recognition Testing

```python
# Test face recognition accuracy
python -c "
import face_recognition
import cv2
# Add your test code here
"
```

## 📊 Database Schema

### Voter Table
```sql
CREATE TABLE voter (
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    email VARCHAR(120) UNIQUE NOT NULL,
    password_hash VARCHAR(128) NOT NULL,
    face_encoding TEXT,
    is_verified BOOLEAN DEFAULT FALSE,
    registration_date DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

### Election Table
```sql
CREATE TABLE election (
    id INTEGER PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    description TEXT,
    start_date DATETIME NOT NULL,
    end_date DATETIME NOT NULL,
    is_active BOOLEAN DEFAULT TRUE,
    created_by INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
```

## 🚀 Deployment

### Local Development
```bash
python app.py
```

### Production Deployment

#### Using Gunicorn
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

#### Using Docker
```dockerfile
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

#### Environment Variables for Production
```env
FLASK_ENV=production
DATABASE_URL=postgresql://...
MAIL_SERVER=smtp.gmail.com
MAIL_USERNAME=production-email@gmail.com
MAIL_PASSWORD=app-password
SECRET_KEY=production-secret-key
```

## 🐛 Troubleshooting

### Common Issues

1. **Face Recognition Not Working**
```bash
# Install cmake and dlib
pip install cmake
pip install dlib
```

2. **Email Not Sending**
```bash
# Check Gmail app password
# Verify SMTP settings in config.py
```

3. **Database Errors**
```bash
# Reset database
rm instance/voters.db
python app.py
```

4. **OpenCV Issues**
```bash
# Reinstall OpenCV
pip uninstall opencv-python
pip install opencv-python
```

## 📈 Performance Optimization

### Face Recognition Optimization
- **Frame Sampling**: Capture every 2nd frame for efficiency
- **Image Compression**: JPEG compression for network transfer
- **Encoding Caching**: Cache face encodings for faster comparison

### Database Optimization
- **Indexing**: Add indexes on frequently queried columns
- **Connection Pooling**: Use SQLAlchemy connection pooling
- **Query Optimization**: Optimize complex queries

## 🤝 Contributing

1. Fork the repository
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Guidelines
- Follow PEP 8 style guide
- Add docstrings to functions
- Write unit tests for new features
- Update documentation

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👥 Authors

- **Sukesh Kumar** - *Initial work* - [sukesh2294@gmail.com](mailto:sukesh2294@gmail.com)
- **Sudhanshu Kumar** - *Co-developer* - [sudhanshujii78@gmail.com](mailto:sudhanshujii78@gmail.com)

## 🙏 Acknowledgments

- Flask community for excellent documentation
- OpenCV team for computer vision capabilities
- dlib library for face recognition algorithms
- Contributors and testers

## 📞 Support

For support, email sukesh2294@gmail.com or create an issue in the GitHub repository.

---

**⭐ Star this repository if you found it helpful!**

Made with ❤️ in India 🇮🇳
