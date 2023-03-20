from rest_framework import serializers
from .models import Vendors, Category, Booking, Services


class VendorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vendors
        fields = ('vendors_user','title','image','contact','description')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title', 'image']