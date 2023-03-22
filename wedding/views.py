from django.shortcuts import render

from wedding.models import WeddingEvent
from wedding.serializers import WeddingEventSerializer
from rest_framework.generics import ListCreateAPIView
from django import forms
from .models import WeddingEvent

# Create your views here.


# ------- check this -----------
class WeddingEventView(ListCreateAPIView):
    queryset = WeddingEvent.objects.all()
    serializer_class = WeddingEventSerializer



# Invitations missing