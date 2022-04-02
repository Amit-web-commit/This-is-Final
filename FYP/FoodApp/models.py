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
  ChoiceProduct = (
    ('LocalProduct', 'LocalProduct'),
    ('SpecialProduct', 'SpecialProduct'),
    ('EditProduct', ' EditProduct'),
    ('ComboPackage', 'ComboPackage'),
  )
  localProductimage = models.ImageField(upload_to='images/')
  name = models.CharField(max_length=30)
  Detail = models.TextField( default='SOME STRING')
  price  = models.IntegerField()
  actualPrice = models.IntegerField(default=1)
  productType = models.CharField(max_length=30, choices= ChoiceProduct, default=1)
  def __str__(self):
      return self.name

  

class SpecialProduct(models.Model):
  specialProductimage = models.ImageField(upload_to='images/')
  name = models.CharField(max_length=30)
  price  = models.IntegerField()
  def __str__(self):
      return self.name

class Order(models.Model):
  customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True)
  date_ordered = models.DateTimeField(auto_now_add =True)
  transaction_id = models.CharField(max_length=100)
  def __str__(self):
    return str(self.id)

  @property
  def get_cart_total(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.get_local_total for item in orderitems])
    return total
  @property
  def get_itemtotal(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.quantity for item in orderitems])
    return total
  @property
  def vat(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.get_local_total for item in orderitems])*0.05
    return total

  @property
  def grant_total(self):
    orderitems = self.orderitem_set.all()
    total = sum([item.get_local_total for item in orderitems])*0.05 +  sum([item.get_local_total for item in orderitems])
    return total
  @property
  def convertDollar(self):
    orderitems = self.orderitem_set.all()
    total = 0.0082 * (sum ([item.get_local_total for item in orderitems])*0.05 +  sum([item.get_local_total for item in orderitems]))
    return total

 

class OrderItem(models.Model):
  # product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True)
  localProduct = models.ForeignKey(LocalProduct, on_delete=models.SET_NULL, blank=True, null=True)
  # specialProduct = models.ForeignKey(SpecialProduct, on_delete=models.SET_NULL, blank=True, null=True)
  # comboPackage = models.ForeignKey(ComboPackage,  on_delete=models.SET_NULL, blank=True, null=True)
  order = models.ForeignKey(Order,on_delete=models.SET_NULL, blank=True, null=True)
  quantity = models.IntegerField(default=1, null=True, blank=True)

  def __str__(self):
      return self.localProduct.name
  
  @property
  def get_local_total(self):
    total = self.localProduct.price  * self.quantity
    if total == 0:
      self.delete()
    return total
 
 
 

  # def vat(self):
  #   return (get_cart_total() * 5/100)
  
  # def grantTotal(self):
  #   return ((self.localProduct.price * self.quantity)+ (self.localProduct.price * self.quantity) * 5/100)
     
  
  

    

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

class CustomizeMenu(models.Model):
  cusineChoices = (
    ('Indian', 'Indian'),
    ('Chinise', 'Chinise'),
    ('Italian', 'Italian'),
    ('Continental', 'Continental'),
    ('Italian', 'Italian'),
  )
  customerName = models.CharField(max_length=100)
  customerEmail =models.EmailField()
  cusineType = models.CharField(max_length=30)
  cusineName = models.CharField(max_length=30)
  ingridents1 = models.CharField(max_length=30)
  ingridents2 = models.CharField(max_length=30)
  ingridents3 = models.CharField(max_length=30)
  recipeDetail = models.TextField()

  def __str__(self):
    return self.customerName

class ReserveTable(models.Model):
  tableChoices = (
    ('Table No 1','Table No 1' ),
    ('Table No 2','Table No 2' ),
    ('Table No 3','Table No 3' ),
    ('Table No 4','Table No 4' ),
    ('Table No 5','Table No 5' ),
    ('Table No 6','Table No 6' ),
    ('Table No 7','Table No 7' ),
    ('Table No 8','Table No 8' ),
    ('Table No 9','Table No 9' ),
    ('Table No 10','Table No 10' ),
  )
  selectHour = (
    ('9AM To 11AM', '9AM To 11AM'),
    ('12AM To 2PM', '12AM To 2PM'),
    ('3PM To 5PM', '3PM To 5PM'),
    ('6PM To 8PM', '6PM To 8PM'),
  )
  totalPerson = (
    ('1 Person','1 Person'),
    ('2 Person','2 Person'),
    ('3 Person','3 Person'),
    ('4 Person','4 Person'),
    ('5 Person','5 Person'),
    ('Larger Party', 'Larger party'),
  )
  user = models.ForeignKey(User, on_delete= models.CASCADE)
  tableNo = models. CharField(max_length=50)
  date = models.DateField()
  selecthour = models.CharField(max_length=50)
  name = models.CharField(max_length=30)
  email = models.EmailField()
  person = models.CharField(max_length=50)

  def __str__(self):
    return self.name


  

