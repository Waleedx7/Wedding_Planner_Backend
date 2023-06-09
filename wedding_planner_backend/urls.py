"""wedding_planner_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path , include
from users import views as user_views
from vendors import views as vendor_views
from wedding import views as wedding_view
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
# flutter endpoints
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', vendor_views.home, name='home'),
    path('api/token/', user_views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/register/', user_views.RegisterView.as_view(), name='register'),
    path('api/login/', user_views.LoginView.as_view(), name='login'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('vendor/', include('vendors.urls')),
    path('api/vendor/services/', vendor_views.ServicesView.as_view(), name = 'services'),#not sure
    path('api/vendor/service/booking/', vendor_views.BookingListView.as_view(), name='book'), #not sure
    path('api/vendor/service/booking/create/', vendor_views.CreateBookingListView.as_view(), name='book-service'), #not sure
    path('api/wedding_event/', wedding_view.WeddingEventView.as_view(), name='wedding-event'), # not sure 

]

    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
