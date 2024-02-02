from django.db import models

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guest = models.IntegerField()
    Booking_date = models.DateField()


class MenuItem(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(decimal_places=2,max_digits=5)
    Inventory = models.IntegerField()