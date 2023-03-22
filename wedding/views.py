from django.shortcuts import render

from wedding.models import WeddingEvent
from wedding.serializers import WeddingEventSerializer
from rest_framework.generics import ListAPIView
from django import forms
from .models import WeddingEvent

# Create your views here.


# ------- check this -----------
class WeddingEventView(ListAPIView):
    queryset = WeddingEvent.objects.all()
    serializer_class = WeddingEventSerializer






class WeddingEvent(forms.ModelForm):
    class Meta:
        model = WeddingEvent
        fields = ["user", "gender", "date","budget"]


# Invitations missing