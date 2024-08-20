from menu.models import Categories,Size,Faqs,Product,DesignImage,ModelImage
from rest_framework import serializers

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields =['id','size','price'] 

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faqs
        fields = ['id','title','content']        

class DesignImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DesignImage
        fields ='__all__'

class ModelImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelImage
        fields =['id','size','glb_file']

class ModelImageSizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ModelImage
        fields = ['size']

class CategorySerializer(serializers.ModelSerializer):
    categories_size = serializers.SerializerMethodField()
    categories_faqs= serializers.SerializerMethodField()
    
    class Meta:
        model = Categories
        fields = ['id','name','slug','meta_title','meta_description','categories_size','categories_faqs']  
    
    def get_categories_size(self, instance):
        query = Size.objects.filter(category_id=int(instance.id), status=1)
        return SizeSerializer(query, many=True).data
    
    def get_categories_faqs(self, instance):
        query = Faqs.objects.filter(category_id=int(instance.id), status=1)
        return FaqSerializer(query, many=True).data

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['id','name','slug'] 

class ProductSerializer(serializers.ModelSerializer):
    size = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = ['id','category','product_name','slug','size','product_list_image','description']
    
    def get_size(self, instance):
        query = ModelImage.objects.filter(product_id=int(instance.id), status=1)
        return ModelImageSizeSerializer(query, many=True).data

class ProductDeatilsSerializer(serializers.ModelSerializer):
    product_design_image = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['id','category','product_name','product_design_image']

    def get_product_design_image(self, instance):
        query = DesignImage.objects.filter(product_id=int(instance.id), status=1)
        return DesignImageSerializer(query, many=True).data  
    

 
     
        