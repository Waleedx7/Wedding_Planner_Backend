from django.db import models
from django.contrib.auth.models import User
from wedding.models import WeddingEvent
# from datetimewidget.widgets import DateTimeWidget
import datetime 

# Create your models here.
class Vendors(models.Model):
    vendors_user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="vendor")
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    contact = models.CharField(max_length=50)
    description = models.TextField()
    category = models.ManyToManyField('Category', related_name='category_vendor')

    def __str__(self):
        return self.title 


class Category(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images/')
    # vendors = models.ForeignKey(Vendors, on_delete=models.CASCADE, related_name='vendors_category')

    def __str__(self):
        return self.title
        
class Services(models.Model):

    title = models.CharField(max_length=50)
    price = models.IntegerField()
    vendors = models.ForeignKey(Vendors, on_delete=models.CASCADE, related_name='vendors_services',default='services_vendor')
    category = models.ManyToManyField('Category', related_name='category_serves') # work on this 
    description = models.TextField()

class Booking(models.Model):
    wedding_event = models.ForeignKey(WeddingEvent, on_delete=models.CASCADE, related_name='bookings')
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name='vendors_booking')
    booking_date = models.DateField(blank=True, default=datetime.date.today)
    