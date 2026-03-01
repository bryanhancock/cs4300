from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Movie, Seat, Booking
import datetime

class MovieModelTest(TestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Test Description",
            release_date=datetime.date(2024, 1, 1),
            duration=120
        )

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.duration, 120)

    def test_movie_str(self):
        self.assertEqual(str(self.movie), "Test Movie")


class SeatModelTest(TestCase):
    def setUp(self):
        self.seat = Seat.objects.create(seat_number="A1")

    def test_seat_creation(self):
        self.assertEqual(self.seat.seat_number, "A1")
        self.assertFalse(self.seat.is_booked)

    def test_seat_str(self):
        self.assertIn("A1", str(self.seat))


class BookingModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="pass123")
        self.movie = Movie.objects.create(
            title="Test Movie",
            description="Desc",
            release_date=datetime.date(2024, 1, 1),
            duration=120
        )
        self.seat = Seat.objects.create(seat_number="B1")
        self.booking = Booking.objects.create(
            movie=self.movie, seat=self.seat, user=self.user
        )

    def test_booking_creation(self):
        self.assertEqual(self.booking.movie.title, "Test Movie")
        self.assertEqual(self.booking.seat.seat_number, "B1")

    def test_booking_str(self):
        self.assertIn("testuser", str(self.booking))


# --- API Integration Tests ---

class MovieAPITest(APITestCase):
    def setUp(self):
        self.movie = Movie.objects.create(
            title="API Movie",
            description="API Desc",
            release_date=datetime.date(2024, 1, 1),
            duration=100
        )

    def test_list_movies(self):
        response = self.client.get('/api/movies/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_movie(self):
        data = {"title": "New Movie", "description": "Desc", "release_date": "2024-06-01", "duration": 90}
        response = self.client.post('/api/movies/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Movie.objects.count(), 2)

    def test_get_single_movie(self):
        response = self.client.get(f'/api/movies/{self.movie.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "API Movie")

    def test_update_movie(self):
        data = {"title": "Updated", "description": "Desc", "release_date": "2024-06-01", "duration": 90}
        response = self.client.put(f'/api/movies/{self.movie.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Updated")

    def test_delete_movie(self):
        response = self.client.delete(f'/api/movies/{self.movie.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Movie.objects.count(), 0)


class SeatAPITest(APITestCase):
    def setUp(self):
        self.seat = Seat.objects.create(seat_number="A1")
        Seat.objects.create(seat_number="A2", is_booked=True)

    def test_list_seats(self):
        response = self.client.get('/api/seats/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_available_seats(self):
        response = self.client.get('/api/seats/available/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['seat_number'], "A1")


class BookingAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="booker", password="pass123")
        self.movie = Movie.objects.create(
            title="Booking Movie",
            description="Desc",
            release_date=datetime.date(2024, 1, 1),
            duration=120
        )
        self.seat = Seat.objects.create(seat_number="C1")
        self.booked_seat = Seat.objects.create(seat_number="C2", is_booked=True)

    def test_create_booking(self):
        data = {"movie": self.movie.id, "seat": self.seat.id, "user": self.user.id}
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.seat.refresh_from_db()
        self.assertTrue(self.seat.is_booked)

    def test_double_booking_fails(self):
        data = {"movie": self.movie.id, "seat": self.booked_seat.id, "user": self.user.id}
        response = self.client.post('/api/bookings/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_bookings(self):
        response = self.client.get('/api/bookings/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


# --- Template View Tests ---

class TemplateViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username="viewuser", password="pass123")
        self.movie = Movie.objects.create(
            title="View Movie",
            description="Desc",
            release_date=datetime.date(2024, 1, 1),
            duration=100
        )
        Seat.objects.create(seat_number="D1")

    def test_movie_list_view(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "View Movie")

    def test_seat_booking_view(self):
        response = self.client.get(f'/book/{self.movie.id}/')
        self.assertEqual(response.status_code, 200)

    def test_booking_history_view(self):
        response = self.client.get('/history/')
        self.assertEqual(response.status_code, 200)

    def test_login_view(self):
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_register_view(self):
        response = self.client.get('/register/')
        self.assertEqual(response.status_code, 200)

    def test_book_seat_post(self):
        self.client.login(username="viewuser", password="pass123")
        seat = Seat.objects.get(seat_number="D1")
        response = self.client.post(f'/book/{self.movie.id}/', {'seat_id': seat.id})
        self.assertEqual(response.status_code, 302)  # redirect after booking
