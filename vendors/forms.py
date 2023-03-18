from django import forms 
from .models import Vendors


class VendorsForm(forms.ModelForm):

    class Meta:
        model = Vendors
        fields = ('vendors_user', 'title','image','price','contact','description')
