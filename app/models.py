from django.db import models
from django.utils.text import slugify
from django.db import models
from autoslug import AutoSlugField
from ckeditor.fields import RichTextField


# -----------------start models------------------

class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='category/')

    def __str__(self):
        return self.name


class Car(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"



class Booking(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    contact_no = models.CharField(max_length=10)
    email = models.EmailField()
    pickup_date = models.DateField()
    return_date = models.DateField()
    # Add more fields as per your requirements

    def __str__(self):
        return self.name



# -------------------Packages-----------------------------------

class PackagesCategory(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    image = models.ImageField(upload_to='Packages_Category/')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Packages(models.Model):
    packages_category = models.ForeignKey(PackagesCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='Packages/')
    des = RichTextField()
    # Add other fields as per your requirements

    def __str__(self):
        return self.name

class PackageDetails(models.Model):
    package = models.ForeignKey(Packages, on_delete=models.CASCADE)
    # Add other fields as per your requirements

    def __str__(self):
        return self.package.name




# -----------Testimonial--------------------
class Testimonial(models.Model):
    content = models.TextField()
    author = models.CharField(max_length=100)
    author_image = models.ImageField(upload_to='testimonial_images')
    rating = models.PositiveIntegerField(default=0)
    

    def __str__(self):
        return self.author



# -----------instagram--------------------
class Instagram(models.Model):
    instagram_image = models.ImageField(upload_to='instagram_image')
    link = models.CharField(max_length=200)
    
    

    def __str__(self):
        return self.link
    


# -----------gallery--------------------
class Gallery(models.Model):
    gallery_image = models.ImageField(upload_to='gallery')
    gallery_name = models.CharField(max_length=100)
    
    

    def __str__(self):
        return self.gallery_name
    




# -----------contact------------------------

class Contact(models.Model):
	name = models.CharField(max_length=255,blank=True,null=True)
	phone = models.CharField(max_length=255,blank=True,null=True)
	email = models.CharField(max_length=255,blank=True,null=True)
	subject = models.CharField(max_length=255,blank=True,null=True)
	message = models.TextField(blank=True,null=True)

	def __str__(self):
		return self.name

        
# -----------Subscribe for updates------------------------

class Subscribe(models.Model):
	subscribe_name = models.CharField(max_length=255,blank=True,null=True)
	subscribe_email = models.CharField(max_length=255,blank=True,null=True)
	

	def __str__(self):
		return self.subscribe_name
