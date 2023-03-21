from django.shortcuts import render

from wedding.models import WeddingEvent
from wedding.serializers import WeddingEventSerializer
from rest_framework.generics import ListAPIView
# Create your views here.


# ------- check this -----------
class WeddingEventView(ListAPIView):
    queryset = WeddingEvent.objects.all()
    serializer_class = WeddingEventSerializer

# Invitations missing