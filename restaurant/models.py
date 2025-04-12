"""
Defines the database models for the restaurant application.
Includes models for Booking and Menu items.
"""
from django.db import models

# Booking Model


class Booking(models.Model):
    """Represents a booking made by a customer."""
    ID = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    Name = models.CharField(max_length=255)  # varchar(255)
    No_of_guests = models.IntegerField()  # int(6)
    BookingDate = models.DateTimeField()  # datetime

    def __str__(self):
        return f'{self.Name} - {self.BookingDate}'

# Menu Model


class Menu(models.Model):
    """Represents a menu item in the restaurant."""
    ID = models.AutoField(primary_key=True)  # Auto-incrementing primary key
    Title = models.CharField(max_length=255)  # varchar(255)
    Price = models.DecimalField(
        max_digits=10, decimal_places=2)  # decimal(10,2)
    Inventory = models.IntegerField()  # int(5)

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'
