from django.urls import path
from . import views

urlpatterns = [
    path('', views.vendor_list, name='vendor_list'),
    path('create/', views.create_vendor, name='create_vendor'),
    path('update/<int:vendor_id>/', views.update_vendor, name='update_vendor'),
    path('delete/<int:vendor_id>/', views.delete_vendor, name='delete_vendor'),
]
