from django.shortcuts import render
from .models import User, Shop, Product, MatchUserProduct
from .serializers import UserSerializer, ShopSerializer, ProductSerializer, MatchUserProductSerializer, UserSignupSerializer, UserLoginSerializer
from rest_framework import generics, status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate


class UserLogin(generics.GenericAPIView):
    serializer_class = UserLoginSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(email=serializer.validated_data['email'])
        if user is not None:
            return Response({
                'user_id': user.pk,
                'email': user.email,
                'username': user.username
            })
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

class UserSignup(generics.CreateAPIView):
    serializer_class = UserSignupSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            'user_id': user.pk,
            'email': user.email
        })

class CurrentUser(generics.RetrieveAPIView):
    def get_object(self):
        return self.request.user
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class ShopListCreate(generics.ListCreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

class ShopRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = [AllowAny]

class ProductListCreate(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class ProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]

class MatchUserProductListCreate(generics.ListCreateAPIView):
    queryset = MatchUserProduct.objects.all()
    serializer_class = MatchUserProductSerializer
    permission_classes = [AllowAny]

class MatchUserProductRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = MatchUserProduct.objects.all()
    serializer_class = MatchUserProductSerializer
    permission_classes = [AllowAny]

class MatchUser(generics.ListCreateAPIView):
    queryset = MatchUserProduct.objects.all()
    serializer_class = MatchUserProductSerializer
    permission_classes = [AllowAny]
    def get_queryset(self):
        return MatchUserProduct.objects.filter(user=self.request.user)

