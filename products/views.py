from rest_framework import viewsets

from .filters import MahsulotlarFilter
from .models import Mahsulotlar
from .serializers import MahsulotlarSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Mahsulotlar
from .serializers import MahsulotlarSerializer
from rest_framework import status
from rest_framework import generics
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend



class MahsulotlarViewSet(viewsets.ModelViewSet):
    queryset = Mahsulotlar.objects.all()
    serializer_class = MahsulotlarSerializer

class MahsulotlarFilterView(generics.ListAPIView):
    queryset = Mahsulotlar.objects.all()
    serializer_class = MahsulotlarSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = MahsulotlarFilter
