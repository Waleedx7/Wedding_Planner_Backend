from django.db import models
from django.contrib.auth.models import User
import datetime 

# Create your models here.
class Gender(models.TextChoices):
        DEFUALT = ('D', "اختر الجنس")
        MALE =  ('MALE', " ذكر")
        FEMALE = ('FEMALE', " أنثى")

class WeddingEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wedding_event')
    gender = models.CharField(
        max_length = 10,
        choices = Gender.choices,
        default=Gender.DEFUALT
        )
    date =  models.DateField(['Date'],default=datetime.date.today) # Use the widget in your form template page as Jinja Tag
    budget = models.IntegerField()

    def __str__(self):
        return  self.date, self.user
    
    
class Invitations(models.Model):
    wedding_event = models.ForeignKey(WeddingEvent, on_delete=models.CASCADE, related_name='invitations')
    guest = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.guest, self.email, self.phone