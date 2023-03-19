
from django.shortcuts import render, redirect , get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .forms import VendorsForm
from .models import Vendors


def home(request):
    return render(request, 'home.html')

def vendor_admin(user):
    return user.groups.filter(name='VendorAdmin').exists()


@user_passes_test(vendor_admin)

def vendor_list(request):
    vendors = Vendors.objects.all()
    return render(request, 'vendor_list.html', {'vendors': vendors})


@user_passes_test(vendor_admin)

def create_vendor(request):
    form = VendorsForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('vendor_list')
    return render(request, 'create_vendor.html', {'form': form})

@user_passes_test(vendor_admin)

def update_vendor(request,vendor_id):
    vendor = get_object_or_404(Vendors, id=vendor_id)
    form = VendorsForm(request.POST or None, request.FILES or None, instance=vendor)
    if request.method == 'POST'and form.is_valid():
        form.save()
        return redirect('vendor_list')
    return render(request, 'update_vendor.html', {'form': form})

@user_passes_test(vendor_admin)

def delete_vendor(request,vendor_id):
    vendor = get_object_or_404(Vendors, id=vendor_id)
    if request.method == 'POST':
        vendor.delete()
        return redirect('vendor_list')
    return render(request, 'delete_vendor.html', {'vendor': vendor})
