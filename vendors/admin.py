from django.contrib import admin

from vendors.models import Vendors,Category,Services,Booking

# Register your models here.

admin.register(Vendors)
admin.register(Category)
admin.register(Services)
admin.register(Booking)
