from django.urls import path
from . import views
from .views import VendorsView , CategoryView

urlpatterns = [
    path('list/', views.vendor_list, name='vendor_list'),
    path('category/', views.category_list, name='category_vendors'),
    path('create/', views.create_vendor, name='create_vendor'),
    path('create/services/', views.create_services, name='create_services'),
    path('create/category/', views.create_category, name='create_category'),
    path('update/<int:vendor_id>/', views.update_vendor, name='update_vendor'),
    path('delete/<int:vendor_id>/', views.delete_vendor, name='delete_vendor'),
    path('api/vendors/', VendorsView.as_view(), name='VendorsList'),
    path('api/categories/', CategoryView.as_view(), name='CategoryList'),
    
]
