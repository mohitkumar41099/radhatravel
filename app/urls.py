
from django.contrib import admin
from django.urls import path, include

from . import views
from django.conf.urls.static import static
from django.conf import settings
from app.views import select_category, select_car, book_car, booking_success



urlpatterns = [



    path('',views.home,name="home"),
    path('home',views.home,name="home"),
    path('contact',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('services/',views.services,name="services"),
    path('select-category/', select_category, name='select_category'),
    path('select-car/<int:category_id>/', select_car, name='select_car'),
    path('book-car/<int:car_id>/', book_car, name='book_car'),

    path('packages-category/', views.packages_category, name='packages_category'),
    path('packages/<slug:packages_category_slug>/', views.packages, name='packages'),
    path('package-details/<int:package_id>/', views.package_details, name='package_details'),


    path('booking-success/', booking_success, name='booking_success'),
    path('contact-success', views.contact_success, name='contact_success')

    # Add more URLs if needed



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


