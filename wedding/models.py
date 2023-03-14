from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class WeddingEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='wedding_event')
    gender = models.BooleanField(default=False) #bride or groom
    date = models.DateField()
    budget = models.IntegerField()

    def __str__(self):
        return self.gender, self.date, self.user
    
    
class Invitations(models.Model):
    wedding_event = models.ForeignKey(WeddingEvent, on_delete=models.CASCADE, related_name='wedding_event_invitations')
    guest = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.guest, self.email, self.phone