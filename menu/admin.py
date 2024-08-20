from django.contrib import admin
from menu.models import Categories,Size,Faqs,Product,DesignImage,ModelImage

# Register your models here.

admin.site.site_header = "Printago Administration"
admin.site.index_title = "Welcome to Printago"

class AdminSize(admin.StackedInline):
    model = Size 
    extra = 0

class AdminFaqs(admin.StackedInline):
    model = Faqs 
    extra = 0

class AdminDesignImage(admin.StackedInline):
    model = DesignImage 
    extra = 0

class AdminModelImage(admin.StackedInline):
    model = ModelImage 
    extra = 0    

class AdminCategories(admin.ModelAdmin):
    list_display=['name','slug','priority','status']
    list_editable = ['priority','status']
    search_fields = ['name']
    list_per_page = 10
    inlines = [AdminSize,AdminFaqs]

class AdminProducts(admin.ModelAdmin):
    list_display=['category','product_name','product_list_image','slug','priority','status']
    list_editable = ['priority','status']
    search_fields = ['product_name']
    list_filter = ['category']
    list_per_page = 10
    inlines = [AdminDesignImage,AdminModelImage]

admin.site.register(Categories,AdminCategories)
admin.site.register(Product,AdminProducts)