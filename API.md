# API Documentation

Smart Voting System REST API documentation for developers.

## Base URL

```
Development: http://localhost:5000
Production: https://your-domain.com
```

## Authentication

The API uses session-based authentication. Some endpoints require user or admin authentication.

### Authentication Types
- **Public**: No authentication required
- **User**: Requires logged-in voter
- **Admin**: Requires logged-in administrator
- **OTP**: Requires OTP verification

## Content Types

All API endpoints accept and return JSON unless otherwise specified.

```http
Content-Type: application/json
Accept: application/json
```

## Error Responses

All errors follow this format:

```json
{
    "success": false,
    "error": "Error description",
    "code": "ERROR_CODE"
}
```

### HTTP Status Codes
- `200` - Success
- `400` - Bad Request
- `401` - Unauthorized
- `403` - Forbidden
- `404` - Not Found
- `429` - Too Many Requests
- `500` - Internal Server Error

## Face Recognition APIs

### Start Face Scanning

Initialize face scanning session for registration.

**Endpoint**: `POST /api/start-face-scan`

**Authentication**: None

**Request Body**:
```json
{
    "aadhar_number": "string"  // Optional, defaults to email
}
```

**Response**:
```json
{
    "message": "Face scanning started",
    "user_id": "user@example.com",
    "total_frames_needed": 51
}
```

---

### Process Face Frame

Process individual face frame during registration.

**Endpoint**: `POST /api/process-face-frame`

**Authentication**: None

**Request Body**:
```json
{
    "email": "user@example.com",
    "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ...",
    "aadhar_number": "optional_string"
}
```

**Response**:
```json
{
    "face_detected": true,
    "frames_captured": 25,
    "total_frames_needed": 51,
    "is_complete": false,
    "progress_percentage": 49.02,
    "registration_success": false,
    "step": 2
}
```

**Complete Response** (when `is_complete: true`):
```json
{
    "face_detected": true,
    "frames_captured": 51,
    "total_frames_needed": 51,
    "is_complete": true,
    "progress_percentage": 100,
    "registration_success": true,
    "message": "Face registration completed successfully",
    "step": 3
}
```

---

## Registration APIs

### Step 1: Email and Password

Register voter with email and password.

**Endpoint**: `POST /register/step1`

**Authentication**: None

**Request Body**:
```json
{
    "email": "user@example.com",
    "first_name": "John Doe",
    "password": "secure_password123"
}
```

**Response**:
```json
{
    "success": true,
    "message": "OTP sent to your email",
    "step": 2
}
```

---

### Step 2: OTP Verification

Verify email with OTP code.

**Endpoint**: `POST /register/step2`

**Authentication**: None

**Request Body**:
```json
{
    "otp": "123456"
}
```

**Response**:
```json
{
    "success": true,
    "message": "OTP verified successfully",
    "step": 3
}
```

---

### Step 3: Complete Registration

Finalize registration after face capture.

**Endpoint**: `GET /register/step3`

**Authentication**: Session

**Response**: HTML page or redirect

---

## Authentication APIs

### Voter Login Step 1

Start voter login process.

**Endpoint**: `POST /voter-login/step1`

**Authentication**: None

**Request Body**:
```json
{
    "email": "voter@example.com",
    "password": "password123"
}
```

**Response**:
```json
{
    "success": true,
    "message": "OTP sent to your email",
    "step": 2
}
```

---

### Voter Login Step 2

Verify OTP for voter login.

**Endpoint**: `POST /voter-login/step2`

**Authentication**: Session

**Request Body**:
```json
{
    "otp": "123456"
}
```

**Response**:
```json
{
    "success": true,
    "message": "OTP verified",
    "step": 3
}
```

---

### Voter Login Step 3

Face verification for voter login.

**Endpoint**: `POST /voter-login/step3`

**Authentication**: Session

**Request Body**:
```json
{
    "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ..."
}
```

**Response**:
```json
{
    "success": true,
    "message": "Login successful",
    "redirect": "/voter-dashboard"
}
```

---

## Admin Authentication APIs

### Admin Login Step 1

Start admin login process.

**Endpoint**: `POST /admin-login/step1`

**Authentication**: None

**Request Body**:
```json
{
    "email": "admin@example.com",
    "password": "admin_password"
}
```

**Response**:
```json
{
    "success": true,
    "message": "OTP sent to admin email",
    "step": 2
}
```

---

### Admin Login Step 2

Verify OTP for admin login.

**Endpoint**: `POST /admin-login/step2`

**Authentication**: Session

**Request Body**:
```json
{
    "otp": "123456"
}
```

**Response**:
```json
{
    "success": true,
    "message": "OTP verified",
    "step": 3
}
```

---

### Admin Login Step 3

Face verification for admin login.

**Endpoint**: `POST /admin-login/step3`

**Authentication**: Session

**Request Body**:
```json
{
    "image": "data:image/jpeg;base64,/9j/4AAQSkZJRgABAQAAAQ..."
}
```

**Response**:
```json
{
    "success": true,
    "message": "Admin login successful",
    "redirect": "/admin-dashboard"
}
```

---

## Election Management APIs

### Create Election

Create a new election (Admin only).

**Endpoint**: `POST /admin/create-election`

**Authentication**: Admin

**Request Body**:
```json
{
    "title": "Student Council Election 2025",
    "description": "Annual student council election",
    "start_date": "2025-02-01T09:00:00",
    "end_date": "2025-02-01T17:00:00"
}
```

**Response**:
```json
{
    "success": true,
    "message": "Election created successfully",
    "election_id": 123
}
```

---

### Add Candidate

Add candidate to election (Admin only).

**Endpoint**: `POST /admin/add-candidate`

**Authentication**: Admin

**Request Body** (multipart/form-data):
```
name: "John Smith"
party: "Student Party"
election_id: 123
photo: [file upload]
symbol: [file upload]
```

**Response**:
```json
{
    "success": true,
    "message": "Candidate added successfully",
    "candidate_id": 456
}
```

---

## Voting APIs

### Cast Vote

Cast vote in active election.

**Endpoint**: `POST /vote`

**Authentication**: User

**Request Body**:
```json
{
    "election_id": 123,
    "candidate_id": 456
}
```

**Response**:
```json
{
    "success": true,
    "message": "Vote cast successfully",
    "vote_id": "encrypted_vote_id"
}
```

---

### Get Election Results

Get results for completed election.

**Endpoint**: `GET /api/results/{election_id}`

**Authentication**: Public (for completed elections)

**Response**:
```json
{
    "success": true,
    "election": {
        "id": 123,
        "title": "Student Council Election 2025",
        "status": "completed",
        "total_votes": 150
    },
    "results": [
        {
            "candidate_id": 456,
            "name": "John Smith",
            "party": "Student Party",
            "votes": 75,
            "percentage": 50.0
        },
        {
            "candidate_id": 457,
            "name": "Jane Doe",
            "party": "Academic Party",
            "votes": 75,
            "percentage": 50.0
        }
    ]
}
```

---

## Data Export APIs

### Export Voter List

Export registered voters list (Admin only).

**Endpoint**: `GET /admin/export/voters`

**Authentication**: Admin

**Query Parameters**:
- `format`: `csv` or `pdf`
- `verified_only`: `true` or `false`

**Response**: File download

---

### Export Election Data

Export election results and data (Admin only).

**Endpoint**: `GET /admin/export/election/{election_id}`

**Authentication**: Admin

**Query Parameters**:
- `format`: `csv` or `pdf`
- `include_votes`: `true` or `false`

**Response**: File download

---

## Utility APIs

### Health Check

Check API health status.

**Endpoint**: `GET /api/health`

**Authentication**: None

**Response**:
```json
{
    "status": "healthy",
    "timestamp": "2025-01-05T10:30:00Z",
    "version": "1.0.0",
    "database": "connected",
    "face_recognition": "available"
}
```

---

### Get System Info

Get system information (Admin only).

**Endpoint**: `GET /api/system-info`

**Authentication**: Admin

**Response**:
```json
{
    "version": "1.0.0",
    "total_voters": 150,
    "total_elections": 5,
    "active_elections": 1,
    "system_status": "operational"
}
```

---

## Rate Limiting

API endpoints are rate limited:
- **Registration**: 5 attempts per hour per IP
- **Login**: 10 attempts per hour per IP
- **OTP**: 3 requests per 10 minutes per email
- **Face Processing**: 100 frames per minute per session
- **Voting**: 1 vote per election per user

## SDKs and Libraries

### Python SDK Example

```python
import requests

class VotingSystemAPI:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
    
    def register_voter(self, email, name, password):
        response = self.session.post(
            f"{self.base_url}/register/step1",
            json={
                "email": email,
                "first_name": name,
                "password": password
            }
        )
        return response.json()
    
    def verify_otp(self, otp):
        response = self.session.post(
            f"{self.base_url}/register/step2",
            json={"otp": otp}
        )
        return response.json()

# Usage
api = VotingSystemAPI("http://localhost:5000")
result = api.register_voter("user@example.com", "John Doe", "password123")
```

### JavaScript SDK Example

```javascript
class VotingSystemAPI {
    constructor(baseUrl) {
        this.baseUrl = baseUrl;
    }

    async registerVoter(email, firstName, password) {
        const response = await fetch(`${this.baseUrl}/register/step1`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                email,
                first_name: firstName,
                password
            })
        });
        return response.json();
    }

    async verifyOTP(otp) {
        const response = await fetch(`${this.baseUrl}/register/step2`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ otp })
        });
        return response.json();
    }
}

// Usage
const api = new VotingSystemAPI('http://localhost:5000');
const result = await api.registerVoter('user@example.com', 'John Doe', 'password123');
```

## Webhooks (Future Implementation)

### Election Events
- `election.created`
- `election.started`
- `election.completed`
- `vote.cast`
- `voter.registered`

### Webhook Format
```json
{
    "event": "vote.cast",
    "timestamp": "2025-01-05T10:30:00Z",
    "data": {
        "election_id": 123,
        "voter_id": "encrypted_id",
        "candidate_id": 456
    }
}
```

## Testing

### Test API Endpoints

Use the provided test scripts:

```bash
# Test registration flow
python tests/test_registration.py

# Test voting flow  
python tests/test_voting.py

# Test admin functions
python tests/test_admin.py
```

### Postman Collection

Import the Postman collection from `docs/postman_collection.json` for easy API testing.

---

For more information, contact: sudhanshujii78@gmail.com
