# serializers.py
from rest_framework import serializers
from userapp.models import Carts,Design

class DesignSerializer(serializers.ModelSerializer):
    class Meta:
        model = Design
        fields = ['id','carts','image']

class CartsSerializer(serializers.ModelSerializer):
    designs = DesignSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.ImageField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only=True)
    class Meta:
        model = Carts
        fields = ['uid','pid','orderID','front_image','color_code','text_font','product_price','size','designs','uploaded_images']
    
    def create(self, validated_data):
        uploaded_images = validated_data.pop("uploaded_images")
        carts = Carts.objects.create(**validated_data)
        for image in uploaded_images:
            newproduct_image = Design.objects.create(carts=carts, image=image)
        return carts
  