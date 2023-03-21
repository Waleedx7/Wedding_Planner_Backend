from django.db import models
from django.contrib.auth.models import User
from wedding.models import WeddingEvent
# from datetimewidget.widgets import DateTimeWidget
import datetime 

# Create your models here.
class Vendors(models.Model):
    vendors_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vedors_user')
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    contact = models.CharField(max_length=50)
    description = models.TextField()

class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    # vendors = models.ForeignKey(Vendors, on_delete=models.CASCADE, related_name='vendors_category')


    
class Booking(models.Model):
    wedding_event = models.ForeignKey(WeddingEvent, on_delete=models.CASCADE, related_name='booking')
    price = models.IntegerField()
    vendors = models.ForeignKey(Vendors, on_delete=models.CASCADE, related_name='vendors_booking')
    booking_date = models.DateField(blank=True, default=datetime.date.today)


    
class Services(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    vendors = models.ForeignKey(Vendors, on_delete=models.CASCADE, related_name='vendors_services')
    booking = models.ManyToManyField(Booking, related_name='booking_services')
    description = models.TextField()

