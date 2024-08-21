from rest_framework import generics
from Goods.models import (
    Category, Product, Cart, Banner, SideMenu, ProductImg, CartProduct,
    Order, ProductEnter, FeatureProduct, RecentArticles, FooterBottomImg
)
from .serializers import (
    CategorySerializer, ProductSerializer, CartSerializer,
    BannerSerializer, SideMenuSerializer, ProductImgSerializer,
    CartProductSerializer, OrderSerializer, ProductEnterSerializer,
    FeatureProductSerializer, RecentArticlesSerializer,
    FooterBottomImgSerializer
)
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Category Views
# @method_decorator(login_required(login_url='login'))
class CategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CategoryRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Product Views
class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Cart Views
class CartListCreateAPIView(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

class CartRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

# Banner Views
class BannerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

class BannerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Banner.objects.all()
    serializer_class = BannerSerializer

# SideMenu Views
class SideMenuListCreateAPIView(generics.ListCreateAPIView):
    queryset = SideMenu.objects.all()
    serializer_class = SideMenuSerializer

class SideMenuRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SideMenu.objects.all()
    serializer_class = SideMenuSerializer

# ProductImg Views
class ProductImgListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductImg.objects.all()
    serializer_class = ProductImgSerializer

class ProductImgRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductImg.objects.all()
    serializer_class = ProductImgSerializer

# CartProduct Views
class CartProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

class CartProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartProduct.objects.all()
    serializer_class = CartProductSerializer

# Order Views
class OrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

# ProductEnter Views
class ProductEnterListCreateAPIView(generics.ListCreateAPIView):
    queryset = ProductEnter.objects.all()
    serializer_class = ProductEnterSerializer

class ProductEnterRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ProductEnter.objects.all()
    serializer_class = ProductEnterSerializer

# FeatureProduct Views
class FeatureProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = FeatureProduct.objects.all()
    serializer_class = FeatureProductSerializer

class FeatureProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FeatureProduct.objects.all()
    serializer_class = FeatureProductSerializer

# RecentArticles Views
class RecentArticlesListCreateAPIView(generics.ListCreateAPIView):
    queryset = RecentArticles.objects.all()
    serializer_class = RecentArticlesSerializer

class RecentArticlesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecentArticles.objects.all()
    serializer_class = RecentArticlesSerializer

# FooterBottomImg Views
class FooterBottomImgListCreateAPIView(generics.ListCreateAPIView):
    queryset = FooterBottomImg.objects.all()
    serializer_class = FooterBottomImgSerializer

class FooterBottomImgRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = FooterBottomImg.objects.all()
    serializer_class = FooterBottomImgSerializer
