Feature: Movie Theater Booking
  As a user
  I want to browse movies and book seats
  So that I can enjoy movies at the theater

  Scenario: View movie listings
    Given the database has movies
    When I visit the movie list page
    Then I should see the movie titles

  Scenario: Book an available seat
    Given the database has a movie and an available seat
    When I book that seat for the movie
    Then the booking should be created
    And the seat should be marked as booked

  Scenario: Cannot double book a seat
    Given a seat is already booked
    When I try to book that same seat via the API
    Then I should receive an error response
