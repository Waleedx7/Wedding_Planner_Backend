from django.contrib import admin

from wedding.models import WeddingEvent, Invitations

# Register your models here.

admin.site.register(WeddingEvent)
admin.site.register(Invitations)