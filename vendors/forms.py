from django import forms 
from .models import Booking, Vendors , Category




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['title', 'image']
        

class VendorsForm(forms.ModelForm):

    class Meta:
        model = Vendors
        fields = ('vendors_user','title','image','contact','description','category')


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ('wedding_event','price','vendors','booking_date')