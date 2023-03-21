
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth import logout
from .forms import CategoryForm, ServicesForm, VendorsForm
from .models import Category, Services, Vendors
from .serializers import CategorySerializer, VendorsSerializer
from rest_framework.generics import ListAPIView


def vendor_admin(user):
    return user.groups.filter(name='VendorAdmin').exists()
@user_passes_test(vendor_admin)

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    return redirect('home')

@user_passes_test(vendor_admin)

def create_services(request):
    form = ServicesForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'create_services.html', {'form': form})

@user_passes_test(vendor_admin)

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})
@user_passes_test(vendor_admin)

def create_category(request):
    form = CategoryForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'create_category.html', {'form': form})

@user_passes_test(vendor_admin)

def vendor_list(request):
    vendors = Vendors.objects.all()
    return render(request, 'vendor_list.html', {'vendors': vendors})


@user_passes_test(vendor_admin)

def create_vendor(request):
    form = VendorsForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'create_vendor.html', {'form': form})

@user_passes_test(vendor_admin)

def update_vendor(request,vendor_id):
    vendor = get_object_or_404(Vendors, id=vendor_id)
    form = VendorsForm(request.POST or None, request.FILES or None, instance=vendor)
    if request.method == 'POST'and form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'update_vendor.html', {'form': form})

@user_passes_test(vendor_admin)

def delete_vendor(request,vendor_id):
    vendor = get_object_or_404(Vendors, id=vendor_id)
    if request.method == 'POST':
        vendor.delete()
        return redirect('home')
    return render(request, 'delete_vendor.html', {'vendor': vendor})

# @user_passes_test(vendor_admin)


class VendorsView(ListAPIView):
    queryset = Vendors.objects.all()
    serializer_class = VendorsSerializer

# @user_passes_test(vendor_admin)

class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer