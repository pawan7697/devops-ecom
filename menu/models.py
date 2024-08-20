from django.db import models
from ckeditor.fields import RichTextField

STATUS_CHOICES = (
        (1, 'Active'),
        (0, 'Deactive'),
    )

# Create your models here.
class Categories(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,null = True, blank=False, unique=True)
    priority = models.IntegerField(null = True, blank=True)
    meta_title = models.CharField(max_length=255, null = True, blank=True)
    meta_description = models.TextField(null = True, blank=True)
    status = models.IntegerField(default=1,choices=STATUS_CHOICES)
    class Meta: 
        ordering = ('priority',)

    def __str__(self):
        return str(self.name)

class Size(models.Model):
    size= models.CharField(max_length=255)
    price = models.IntegerField() 
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL,null = True,related_name='categories_size')
    status = models.IntegerField(default=1,choices=STATUS_CHOICES)  

class Faqs(models.Model):
    title= models.CharField(max_length=255)
    content = models.TextField(null = True, blank=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL,null = True,related_name='categories_faqs')
    status = models.IntegerField(default=1,choices=STATUS_CHOICES)

class Product(models.Model):
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL,null = True,related_name='categories_product')
    product_name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255,null = True, blank=False, unique=True)
    product_list_image = models.ImageField(upload_to='list_image/')
    description = RichTextField()
    priority = models.IntegerField(null = True, blank=True)
    status = models.IntegerField(default=1,choices=STATUS_CHOICES)

class DesignImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null = True,related_name='product_design_image')
    title= models.CharField(max_length=255)
    button_image = models.ImageField(upload_to='button_image/')
    full_image = models.ImageField(upload_to='full_image/')
    status = models.IntegerField(default=1,choices=STATUS_CHOICES)

class ModelImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL,null = True,related_name='product_model_image')
    size= models.CharField(max_length=255)
    glb_file = models.FileField(upload_to='glb_file/',null = True, blank=False)
    status = models.IntegerField(default=1,choices=STATUS_CHOICES)
   



