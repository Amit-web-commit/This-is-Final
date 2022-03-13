from django.db import models
from django.urls import *
from django.contrib.auth.models import User
# Create your models here.
class Customer(models.Model):
  user = models.OneToOneField(User, on_delete = models.CASCADE)
  name = models.CharField(max_length=30)
  email = models.EmailField()

  def __str__(self):
    return self.name

class Product(models.Model):

  # foodID = models.IntegerField(primary_key = True)
  productName = models.CharField(max_length=30)
  productDetail = models.TextField()
  productImage = models.ImageField(upload_to='images/')
  slug = models.SlugField(unique=True)
  price  = models.IntegerField()
  # menuID ForeignKey
  # menuID = models.ForeignKey(Menu, on_delete = models.CASCADE())

  def __str__(self):
    return self.productName
  # def get_absolute_url(self):
  #   return reverse('product_detail', kwargs={'slug':self.slug})
class ComboPackage(models.Model):
  productImage = models.ImageField(upload_to='images/')
  productName = models.CharField(max_length=30)
  price  = models.IntegerField()
  actualPrice = models.IntegerField()
  def __str__(self):
      return self.productName
class Team(models.Model):
  POST_CHOICES = (
    ('Manager', 'Manager'),
    ('Accountant', 'Accountant'),
    ('Head Chef', 'Head Chef'),
    ('Assistant Chef', 'Assistant Chef'),
    ('Waiter', 'Waiter'),
  )
  teamProfile = models.ImageField(upload_to='images/')
  name = models.CharField(max_length=30)
  post = models.CharField(max_length=30, choices= POST_CHOICES)
  detail = models.CharField(max_length=100)
  def __str__(self):
      return self.name

class CustomerProfile(models.Model):
  customerProfile = models.ImageField(upload_to='images/')
  name = models.CharField(max_length=30)
  detail = models.CharField(max_length=200)
  def __str__(self):
      return self.name

class LocalProduct(models.Model):
  localProductimage = models.ImageField(upload_to='images/')
  name = models.CharField(max_length=30)
  price  = models.IntegerField()
  def __str__(self):
      return self.name

class SpecialProduct(models.Model):
  specialProductimage = models.ImageField(upload_to='images/')
  name = models.CharField(max_length=30)
  price  = models.IntegerField()
  def __str__(self):
      return self.name

# class Order(models.Model):
#   customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
#   date_ordered = models.DateTimeField(auto_now_add =True)
#   transaction_id = models.CharField(max_length=100)


# class OrderItem(models.Model):
#   product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
#   localProduct = models.ForeignKey(LocalProduct, on_delete=models.SET_NULL, blank=True, null=True)
#   specialProduct = models.ForeignKey(SpecialProduct, on_delete=models.SET_NULL, blank=True, null=True)
#   comboPackage = models.ForeignKey(ComboPackage,  on_delete=models.SET_NULL, blank=True, null=True)
#   quantity = models.IntegerField(default=0, null=True, blank=True)

  

class Menu(models.Model):
  menuID = models.IntegerField(primary_key = True)
  menuDetail = models.TextField()
  slug = models.SlugField(unique=True)
  def __str__(self):
    return self.foodName
  
class ReviewRating(models.Model):
  user = models.ForeignKey(User, on_delete= models.CASCADE)
  product = models.ForeignKey(LocalProduct, on_delete= models.CASCADE)
  review = models.CharField(max_length=200)
  comment = models.CharField(max_length=300)
  rate = models.IntegerField(default=0)

  def __str__(self):
    return self.review
class Contact(models.Model):
    name = models.CharField(max_length = 50)
    email = models.EmailField()
    phone = models.IntegerField()
    message  = models.TextField()
    
    def __str__(self):
        return self.name