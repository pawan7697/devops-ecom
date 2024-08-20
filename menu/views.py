from django.shortcuts import render
from menu.models import Categories,Size,Product,ModelImage
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from menu.serializers import CategorySerializer,SizeSerializer,FaqSerializer,CategoriesSerializer,ProductSerializer,ProductDeatilsSerializer,ModelImageSerializer


# Create your views here.

class CategoriesView(APIView):
    def get(self,request):
      queryset = Categories.objects.filter(status=1)
      serializer_class = CategoriesSerializer(queryset,many=True)
      return Response(serializer_class.data)

class CategorieSizeView(APIView):
    def get(self,request,slugs):
      cat = Categories.objects.filter(slug=slugs,status=1).first().id
      queryset = Size.objects.filter(category_id=cat,status=1)
      serializer_class = SizeSerializer(queryset,many=True)
      return Response(serializer_class.data)
    
class ProductView(APIView):
   def get(self,request,slugs):
      cat = Categories.objects.filter(slug=slugs,status=1).first().id
      queryset = Product.objects.filter(category_id=cat,status=1)
      serializer_class = ProductSerializer(queryset,many=True)
      return Response(serializer_class.data)

class ProductDetailsView(APIView):
   def get(self,request,slugs,size):
      queryset = Product.objects.filter(slug=slugs,status=1).first()
      serializer_class = ProductDeatilsSerializer(queryset)
      query = ModelImage.objects.filter(product_id=int(queryset.id),size=str(size),status=1).first()
      serializer = ModelImageSerializer(query)
      return Response({'product':serializer_class.data,'model':serializer.data})      