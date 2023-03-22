from rest_framework import serializers
from wedding.models import WeddingEvent


# ------- check this ------
class WeddingEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeddingEvent
        fields = ['user', 'gender','date','budget']
        


# Invitations missing