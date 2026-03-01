from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'movies', views.MovieViewSet)
router.register(r'seats', views.SeatViewSet)
router.register(r'bookings', views.BookingViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('', views.movie_list, name='movie_list'),
    path('book/<int:movie_id>/', views.seat_booking, name='book_seat'),
    path('history/', views.booking_history, name='booking_history'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
