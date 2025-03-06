# siargao-tourism-backend

# Visit Siargao API

This repository contains the **Django + Supabase** backend for the Visit Siargao Application.

## Features
- User Registration with Email Verification
- JWT Authentication
- Login & Logout API
- Password Reset with Email
- Explore Places (CRUD)
- Save Search History

## Tech Stack
- **Backend:** Django Rest Framework
- **Database:** Supabase (PostgreSQL)
- **Authentication:** JWT & Supabase

## Setup

### 1. Clone Repository
```bash
git clone https://github.com/username/visit-siargao-backend.git
cd visit-siargao-backend
```

### 2. Virtual Environment
Create a virtual environment and activate it.
```bash
python -m venv env
source env/bin/activate   # Linux/MacOS
env\Scripts\activate    # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Environment Variables
Create a `.env` file in the root directory.

Example:
```env
DEBUG=True
SECRET_KEY=your_secret_key
SUPABASE_URL=https://your-supabase-url.supabase.co
SUPABASE_KEY=your_supabase_api_key
```

### 5. Database Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser
```bash
python manage.py createsuperuser
```

### 7. Run Server
```bash
python manage.py runserver
```

## API Documentation

### Authentication
| Endpoint                 | Method | Description            |
|--------------------------|--------|----------------------|
| `/api/users/`           | POST   | Sign Up             |
| `/api/users/login/`      | POST   | Log In             |
| `/api/users/me/`         | GET    | Get Current User    |
| `/api/users/verify_email/` | POST   | Verify Email       |
| `/api/users/forgot_password/` | POST   | Reset Password    |
| `/api/users/logout/`     | POST   | Log Out            |

### Explore API
| Endpoint         | Method | Description        |
|----------------|--------|------------------|
| `/api/explore/` | GET    | List Places      |
| `/api/explore/` | POST   | Add Place       |
| `/api/explore/:id/` | PUT    | Update Place    |
| `/api/explore/:id/` | DELETE | Delete Place    |

### Search API
| Endpoint       | Method | Description           |
|---------------|--------|---------------------|
| `/api/search/` | GET    | List Search History |
| `/api/search/` | POST   | Save Search        |

## Testing with Postman
Import the Postman collection from the following URL:
[Postman Collection](#)

## Frontend Integration
The frontend will consume the API by making HTTP requests to the endpoints.

Example Axios Request:
```javascript
axios.post('http://127.0.0.1:8000/api/users/login/', {
    email: 'test@gmail.com',
    password: 'password123'
})
.then(response => {
    console.log(response.data.access);
})
.catch(error => {
    console.error(error.response.data);
});
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first.

## License
[MIT License](LICENSE)

