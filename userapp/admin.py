from django.contrib import admin
from userapp.models import SignUp,Carts,OrderItems
from import_export.admin import ImportExportModelAdmin
from django.utils.html import format_html
from django.conf import settings
# Register your models here.

class AdmininSignUp(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','username','email','status']
    list_editable = ['status']
    list_per_page = 20 

class AdmininOrderItems(admin.ModelAdmin):
    list_display=['created_at','uid','order_id','orderSatus']
    # list_editable = ['status']
    list_per_page = 20 
    def order_id(self, obj):
        if obj.orderID:
            return format_html(
            '<a href="http://127.0.0.1:8000/invoice/'+obj.orderID+'" target="_blank" style="color: red; text-decoration: underline;">'+obj.orderID+'</a>',

        )
        else:
            return 'Not Available'

class AdmininCarts(ImportExportModelAdmin,admin.ModelAdmin):
    list_display=['id','uid','color_code','product_price']
    # list_editable = ['status']
    list_per_page = 20 

admin.site.register(SignUp,AdmininSignUp)
admin.site.register(Carts,AdmininCarts)
admin.site.register(OrderItems,AdmininOrderItems)
