from django.db import models
from django.contrib.auth.models import User
import datetime 

# Create your models here.
class Gender(models.TextChoices):
        DEFUALT = ('D', "")
        MALE =  ('Bride', " Bride")
        FEMALE = ('Groom', " Groom")

class WeddingEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wedding_event')
    gender = models.CharField(
        max_length = 10,
        choices = Gender.choices,
        default=Gender.DEFUALT
        )
    date =  models.DateField(['Date'],default=datetime.date.today) # Use the widget in your form template page as Jinja Tag
    budget = models.PositiveIntegerField()
  
    
class Invitations(models.Model):
    wedding_event = models.ForeignKey(WeddingEvent, on_delete=models.CASCADE, related_name='invitations')
    guest = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

   