from django.shortcuts import render
from django.views.generic import TemplateView
from userapp.models import SignUp,Carts,OrderItems,Design
from menu.models import Product
from django.db.models import Sum

# Create your views here.
class CartsImages:
    def AnglesImages(self,cartID):
        return Design.objects.filter(carts_id=cartID)
        


class InvoiceView(TemplateView,CartsImages):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        orderId =self.kwargs.get('orderId')
        userid=OrderItems.objects.filter(orderID=str(orderId)).first().uid_id
        context['invoice_number'] = orderId
        carts_query = Carts.objects.filter(orderID=orderId)
        total_sum = Carts.objects.filter(orderID=orderId).aggregate(total_sum=Sum('product_price'))['total_sum']
        carts_with_images = []
        for cart in carts_query:
            images = self.AnglesImages(cart.id)
            pname = Product.objects.filter(id=int(cart.pid_id)).first()
            carts_with_images.append({
                'cart': cart,
                'images': images,
                'product_name': pname.product_name
            })

        context['carts_with_images'] = carts_with_images
        user = SignUp.objects.filter(id=userid).first()
        context['username'] = user.username
        context['email'] = user.email
        context['grand_total'] = total_sum
        return context

