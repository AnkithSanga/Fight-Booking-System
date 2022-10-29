from django.contrib import admin
from . models import Flight,Booking,Seating
from django.contrib.auth.models import User

admin.site.register(Flight)
admin.site.register(Booking)
admin.site.register(Seating)
