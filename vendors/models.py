from django.db import models
from django.contrib.auth.models import User
from wedding.models import WeddingEvent
# from datetimewidget.widgets import DateTimeWidget
import datetime 

# Create your models here.
class Vendors(models.Model):
    vendors_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vedors_user',default='')
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    price = models.IntegerField()
    contact = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title, self.price, self.contact
    


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    vendors = models.ForeignKey(Vendors, on_delete=models.CASCADE, related_name='vendors_category')

    def __str__(self):
        return self.title, self.vendors
    
class Booking(models.Model):
    wedding_event = models.ForeignKey(WeddingEvent, on_delete=models.CASCADE, related_name='booking')
    service = models.CharField(max_length=50)
    price = models.IntegerField()
    vendors = models.ForeignKey(Vendors, on_delete=models.CASCADE, related_name='vendors_booking')
    booking_date = models.DateField(['Date'],default=datetime.date.today)
    def __str__(self):
        return self.service, self.price,  self.wedding_event
    
class Services(models.Model):
    title = models.CharField(max_length=50)
    price = models.IntegerField()
    vendors = models.ForeignKey(Vendors, on_delete=models.CASCADE, related_name='vendors_services',default='')
    booking = models.ManyToManyField(Booking, related_name='booking_services')
    description = models.TextField()

    def __str__(self):
        return self.title, self.price, self.vendors