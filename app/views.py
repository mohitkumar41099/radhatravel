from django.shortcuts import get_object_or_404, render, redirect
from .forms import BookingForm
from .models import Category, Car, Booking, PackageDetails, PackagesCategory,Packages,Testimonial,Contact,Instagram,Gallery,Subscribe
from django.contrib import messages






def home(request):
    categories = Category.objects.all()
    testimonials = Testimonial.objects.all()
    packages_category = PackagesCategory.objects.all()
    instagram=Instagram.objects.all()
    subscribe=Subscribe.objects.all()
    context ={'testimonials':testimonials,'packages_category':packages_category,'categories':categories,'instagram':instagram,'subscribe':subscribe}


    return render(request, 'index.html',context)

def about(request):
    
    return render(request, 'about.html')


def services(request):
    
    return render(request, 'about.html')




def select_category(request):
    categories = Category.objects.all()
    return render(request, 'select_category.html', {'categories': categories})




def select_car(request, category_id):
    cars = Car.objects.filter(category_id=category_id)
    return render(request, 'select_car.html', {'cars': cars})




def book_car(request, car_id):
    car = Car.objects.get(id=car_id)
    cars = Car.objects.filter(category=car.category)  # Retrieve cars of the same category as the selected car
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('booking_success')
    else:
        form = BookingForm()
    return render(request, 'book_car.html', {'form': form, 'cars': cars})  # Pass the 'cars' queryset to the template






def booking_success(request):
    return render(request, 'booking_success.html')



# pakeages----------------------------


def packages_category(request):
    packages_category = PackagesCategory.objects.all()
    return render(request, 'packages_category.html', {'packages_category': packages_category})

def packages(request,packages_category_slug):
    packages_category = PackagesCategory.objects.all()
    categorys = get_object_or_404(packages_category, slug=packages_category_slug)
    packages = categorys.packages_set.all()
    return render(request, 'packages.html', { 'packages': packages,'categorys':categorys})

def package_details(request, package_id):
    package = get_object_or_404(Packages, id=package_id)
    details = PackageDetails.objects.filter(package=package)
    return render(request, 'package_details.html', {'package': package, 'details': details})






# _____________________________________contact______________________________

def contact(request):
  
    if request.method == 'POST':
        
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        if len(name) > 4:
            contact = Contact(name=name,phone=phone,email=email,subject=subject,message=message)
            contact.save()
            messages.success(request,'Successfully Form Submit')
            return redirect('/contact-success')
        else:
            messages.error(request,'First Name Should Be more then 4 chars')
            return redirect('/contact-success')
    return render(request,'contact.html')

def contact_success(request):
    return render(request, 'contact_success.html')