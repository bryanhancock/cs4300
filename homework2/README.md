# CineBook - Movie Theater Booking Application

A RESTful Movie Theater Booking Application built with Python, Django, and Django REST Framework.

## AI Usage Disclosure
This project was built with assistance from Claude (Anthropic) for code generation, debugging, and project structure guidance. Claude was used to generate boilerplate code for models, views, serializers, templates, and tests. All code was reviewed and understood before submission.

---

## Project Structure
```
homework2/
├── bookings/
│   ├── migrations/
│   ├── templates/
│   │   └── bookings/
│   │       ├── base.html
│   │       ├── movie_list.html
│   │       ├── seat_booking.html
│   │       ├── booking_history.html
│   │       ├── login.html
│   │       └── register.html
│   ├── models.py
│   ├── views.py
│   ├── serializers.py
│   ├── urls.py
│   └── tests.py
├── features/
│   ├── steps/
│   │   └── booking_steps.py
│   ├── environment.py
│   └── booking.feature
├── movie_theater_booking/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── requirements.txt
├── build.sh
└── README.md
```

---

## Features
- View all movie listings via UI and REST API
- Book seats for movies via UI and REST API
- View booking history via UI and REST API
- User registration and login
- Admin panel for managing movies, seats, and bookings
- Responsive UI built with Bootstrap 5

---

## Models
- **Movie** - title, description, release date, duration
- **Seat** - seat number, booking status
- **Booking** - movie, seat, user, booking date

---

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/movies/` | List all movies |
| POST | `/api/movies/` | Create a movie |
| GET | `/api/movies/<id>/` | Get a single movie |
| PUT | `/api/movies/<id>/` | Update a movie |
| DELETE | `/api/movies/<id>/` | Delete a movie |
| GET | `/api/seats/` | List all seats |
| GET | `/api/seats/available/` | List available seats only |
| GET | `/api/bookings/` | List all bookings |
| POST | `/api/bookings/` | Create a booking |

---

## Setup Instructions

### Prerequisites
- Python 3.12+
- pip

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/bryanhancock/cs4300.git
cd cs4300/homework2
```

2. Create and activate a virtual environment:
```bash
python3 -m venv myenv --system-site-packages
source myenv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python3 manage.py migrate
```

5. Create a superuser (for admin panel):
```bash
python3 manage.py createsuperuser
```

6. Start the development server:
```bash
python3 manage.py runserver 0.0.0.0:3000
```

7. Visit `http://localhost:3000` in your browser.

---

## Running Tests

### Unit & Integration Tests with Coverage
```bash
coverage run --source='.' manage.py test bookings --verbosity=2
coverage report
```

### BDD Tests with Behave
```bash
python3 -m behave --no-capture
```

---

## Deployment

This application is deployed on Render.

**Live URL:** https://YOUR_ACTUAL_RENDER_URL_HERE

### Environment Variables required for deployment:
| Variable | Description |
|----------|-------------|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | Set to `False` in production |
| `DATABASE_URL` | PostgreSQL database URL (auto-set by Render) |

### Render Build Settings:
- **Build Command:** `./build.sh`
- **Start Command:** `gunicorn movie_theater_booking.wsgi:application`

---

## Admin Panel
Visit `/admin/` and log in with your superuser credentials to manage movies, seats, and bookings directly.
