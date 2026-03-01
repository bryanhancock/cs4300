from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Movie, Seat, Booking
from .serializers import MovieSerializer, SeatSerializer, BookingSerializer

# --- API ViewSets ---

class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class SeatViewSet(viewsets.ModelViewSet):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer

    @action(detail=False, methods=['get'])
    def available(self, request):
        available_seats = Seat.objects.filter(is_booked=False)
        serializer = self.get_serializer(available_seats, many=True)
        return Response(serializer.data)

class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def create(self, request, *args, **kwargs):
        seat_id = request.data.get('seat')
        seat = get_object_or_404(Seat, id=seat_id)
        if seat.is_booked:
            return Response({'error': 'Seat is already booked.'}, status=status.HTTP_400_BAD_REQUEST)
        seat.is_booked = True
        seat.save()
        return super().create(request, *args, **kwargs)

# --- Template Views ---

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'bookings/movie_list.html', {'movies': movies})

def seat_booking(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    seats = Seat.objects.all()
    if request.method == 'POST':
        seat_id = request.POST.get('seat_id')
        seat = get_object_or_404(Seat, id=seat_id)
        if seat.is_booked:
            messages.error(request, 'That seat is already booked!')
        else:
            user = request.user if request.user.is_authenticated else User.objects.first()
            Booking.objects.create(movie=movie, seat=seat, user=user)
            seat.is_booked = True
            seat.save()
            messages.success(request, f'Seat {seat.seat_number} booked successfully!')
            return redirect('booking_history')
    return render(request, 'bookings/seat_booking.html', {'movie': movie, 'seats': seats})

def booking_history(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
    else:
        bookings = Booking.objects.all()
    return render(request, 'bookings/booking_history.html', {'bookings': bookings})

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('movie_list')
    return render(request, 'bookings/register.html')

def login_view(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('movie_list')
        messages.error(request, 'Invalid credentials.')
    return render(request, 'bookings/login.html')

def logout_view(request):
    logout(request)
    return redirect('movie_list')
