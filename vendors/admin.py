from django.contrib import admin

from vendors.models import Vendors,Category,Services,Booking

# Register your models here.

admin.site.register(Vendors)
admin.site.register(Category)
admin.site.register(Services)
admin.site.register(Booking)