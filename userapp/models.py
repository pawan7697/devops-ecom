from django.db import models
from menu.models import Product
import uuid

STATUS_CHOICES = (
        (1, 'Active'),
        (0, 'Deactive'),
    )

# Create your models here.
class SignUp(models.Model):
    id = models.UUIDField(primary_key = True,default = uuid.uuid4, editable = False)
    username = models.CharField(max_length=255,null = True, blank=False)
    email =  models.EmailField(max_length=255, unique=True) 
    phone = models.CharField(max_length=255,null = True, blank=True)
    gender = models.CharField(max_length=255,null = True, blank=True)
    password = models.CharField(max_length=255)
    name_or_company = models.CharField(max_length=255,null = True, blank=True)
    street1 = models.CharField(max_length=255,null = True, blank=True)
    street2 = models.CharField(max_length=255,null = True, blank=True)
    post_code = models.CharField(max_length=255,null = True, blank=True)
    city = models.CharField(max_length=255,null = True, blank=True)
    language_code = models.CharField(max_length=255,null = True, blank=True)
    country_code = models.CharField(max_length=255,null = True, blank=True)
    status = models.IntegerField(default=1,choices=STATUS_CHOICES)
    def __str__(self):
        return str(self.username)


  
# class Order(models.Model):
#     id = models.UUIDField(default=uuid.uuid4, primary_key=True)
#     created = models.DateTimeField(auto_now_add=True)
    
#     def __str__(self):
#         return str(self.id)
    
class Carts(models.Model):
    uid =  models.ForeignKey(SignUp, on_delete=models.SET_NULL,null = True)
    pid =  models.ForeignKey(Product, on_delete=models.SET_NULL,null = True)
    orderID = models.CharField(max_length=255,null = True, blank=False)
    front_image = models.FileField(upload_to='screenshot/',null = True, blank=True)
    color_code =models.TextField(null = True, blank=True)
    text_font = models.TextField(null = True, blank=True)
    product_price = models.IntegerField()
    size = models.CharField(max_length=255,null = True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True,editable=False,blank=True ,null = True)

class Design(models.Model):
    carts = models.ForeignKey(Carts, on_delete=models.SET_NULL, null = True,related_name = "designs")
    image = models.ImageField(upload_to="designs_img", default="", null=True, blank=True)

  
class Orders(models.Model):
    uid =  models.ForeignKey(SignUp, on_delete=models.SET_NULL,null = True)
    orderID = models.CharField(max_length=255,null = True, blank=False, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.orderID

  
class OrderItems(models.Model):
    uid =  models.ForeignKey(SignUp, on_delete=models.SET_NULL,null = True)
    orderID = models.CharField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    orderSatus = models.CharField(max_length=255, default="Pending",null = True, blank=True)
    
    def __str__(self):
        return self.orderID  
      



