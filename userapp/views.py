from django.shortcuts import render
from userapp.models import SignUp,Carts,Orders,OrderItems
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from userapp.serializers import CartsSerializer
from rest_framework.generics import CreateAPIView,ListCreateAPIView
from rest_framework.parsers import MultiPartParser, FormParser

# Create your views here.

class SignUPView(APIView):
    def post(self, request):
        try:
            username = request.data.get('username')
            email = request.data.get('email')
            password = request.data.get('password')

            if not all([username, email, password]):
                return Response({'status': False, 'message': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
            
            user = SignUp.objects.create(username=username, email=email, password=password)
            return Response({'status': True, 'UId': user.id})
        except Exception as e:
            return Response({'status': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class SignInView(APIView):
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            user = SignUp.objects.filter(email=email, password=password, status=1).first()
            if user:
                user_data = {
                    'uid': user.id,
                    'username': user.username,
                    'email': user.email,
                    
                }
                return Response({'status': True,'message': 'Login successful', 'user_data': user_data}, status=status.HTTP_200_OK)
            else:
                return Response({'status': False,'error': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'status': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class userEditView(APIView):
    def put(self, request):
        try:
            username = request.data.get('username')
            phone = request.data.get('phone')
            gender = request.data.get('gender')
            name_or_company = request.data.get('name_or_company')
            street1 = request.data.get('street1')
            street2 = request.data.get('street2')
            post_code = request.data.get('post_code')
            city = request.data.get('city')
            language_code = request.data.get('language_code')
            country_code = request.data.get('country_code')
            uid = str(request.data.get('uid'))
            if not all([uid,username, name_or_company, street1,street2, post_code,city,language_code,country_code]):
                return Response({'status': False, 'message': 'Missing required fields'}, status=status.HTTP_400_BAD_REQUEST)
            
            user = SignUp.objects.filter(id=uid).update(username=username,phone=phone,gender=gender,name_or_company=name_or_company, street1=street1,street2=street2, post_code=post_code,city=city,language_code=language_code,country_code=country_code)
            return Response({'status': True, 'UId': uid})
        except Exception as e:
            return Response({'status': False, 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

            
class ForgotPasswordAPIView(APIView):
    def post(self, request):
        pass

class CartsView(APIView):
    def post(self, request, format=None):
        
        serializer = CartsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GETCartsView(APIView):
    def get(self, request, uid):
        queryset=Carts.objects.filter(uid=str(uid))
        serializer_class = CartsSerializer(queryset,many=True)
        return Response(serializer_class.data)
 
# class OrderCreateView(ListCreateAPIView):
#     def post(self, request, format=None):
#         serializer = CartsSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        

# class OrderCreateView(ListCreateAPIView):
#     queryset = Carts.objects.all()
#     serializer_class = CartsSerializer
    
#     parser_classes = (MultiPartParser, FormParser)

class OrderCreateView(APIView):
    def post(self, request, format=None):
        serializer = CartsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            try:
                orderID = request.data.get('orderID')
                uid = request.data.get('uid')
                if orderID and uid:
                    OrderItems.objects.create(uid_id=str(uid),orderID=str(orderID))
            except Exception as e:
                # Log the exception
                print(f"Exception occurred: {e}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

