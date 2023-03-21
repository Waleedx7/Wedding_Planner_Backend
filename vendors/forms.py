from django import forms 
from .models import Booking, Services, Vendors , Category




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'image']
        

class VendorsForm(forms.ModelForm):

    class Meta:
        model = Vendors
        fields = ('title','image','contact','description','category')


class ServicesForm(forms.ModelForm):
    class Meta:
        model = Services
        fields = ('title','price','vendors','description')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('wedding_event','service','booking_date')
