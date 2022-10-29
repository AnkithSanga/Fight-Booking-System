from django.db import models
from django.db.models.fields import DateField
from django.contrib.auth.models import User
from datetime import datetime



class Flight(models.Model):
    flight_name = models.CharField(max_length = 150)
    source = models.CharField(max_length = 150)
    destination = models.CharField(max_length = 150)
    capacity = models.IntegerField()
    available_first_class = models.IntegerField()
    available_business_class = models.IntegerField()
    available_economy_class = models.IntegerField()
    

class Booking(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    flight_id = models.ForeignKey(Flight,on_delete=models.CASCADE)
    seat_number = models.IntegerField()

class Seating(models.Model):
    flight_id = models.ForeignKey(Flight,on_delete = models.CASCADE)
    seat_number = models.IntegerField()
    status = models.BooleanField(default = False)

