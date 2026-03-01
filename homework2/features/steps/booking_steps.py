from behave import given, when, then
from django.test import Client
from django.contrib.auth.models import User
from bookings.models import Movie, Seat, Booking
import datetime
import json

@given('the database has movies')
def step_has_movies(context):
    context.movie = Movie.objects.create(
        title="BDD Movie",
        description="BDD Test",
        release_date=datetime.date(2024, 1, 1),
        duration=120
    )

@when('I visit the movie list page')
def step_visit_movie_list(context):
    context.client = Client()
    context.response = context.client.get('/')

@then('I should see the movie titles')
def step_see_movie_titles(context):
    assert context.response.status_code == 200
    assert b"BDD Movie" in context.response.content

@given('the database has a movie and an available seat')
def step_movie_and_seat(context):
    context.user = User.objects.create_user(username='bdduser', password='pass123')
    context.movie = Movie.objects.create(
        title="BDD Booking Movie",
        description="Desc",
        release_date=datetime.date(2024, 1, 1),
        duration=100
    )
    context.seat = Seat.objects.create(seat_number="Z1")

@when('I book that seat for the movie')
def step_book_seat(context):
    from rest_framework.test import APIClient
    context.api_client = APIClient()
    context.response = context.api_client.post('/api/bookings/', {
        'movie': context.movie.id,
        'seat': context.seat.id,
        'user': context.user.id
    })

@then('the booking should be created')
def step_booking_created(context):
    assert context.response.status_code == 201

@then('the seat should be marked as booked')
def step_seat_booked(context):
    context.seat.refresh_from_db()
    assert context.seat.is_booked

@given('a seat is already booked')
def step_seat_already_booked(context):
    context.user = User.objects.create_user(username='bdduser2', password='pass123')
    context.movie = Movie.objects.create(
        title="Double Book Movie",
        description="Desc",
        release_date=datetime.date(2024, 1, 1),
        duration=100
    )
    context.seat = Seat.objects.create(seat_number="Z2", is_booked=True)

@when('I try to book that same seat via the API')
def step_try_double_book(context):
    from rest_framework.test import APIClient
    context.api_client = APIClient()
    context.response = context.api_client.post('/api/bookings/', {
        'movie': context.movie.id,
        'seat': context.seat.id,
        'user': context.user.id
    })

@then('I should receive an error response')
def step_error_response(context):
    assert context.response.status_code == 400
