from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MahsulotlarFilterView, MahsulotlarViewSet


# Router yaratish
router = DefaultRouter()
router.register(r'mahsulotlar', MahsulotlarViewSet)

urlpatterns = [
    path('mahsulotlar/search/', MahsulotlarFilterView.as_view(), name='mahsulotlar-search'),
    path('', include(router.urls)),
]
