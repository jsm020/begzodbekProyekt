import django_filters
from .models import Mahsulotlar

class MahsulotlarFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Mahsulotlar
        fields = ['name', 'min_price', 'max_price']
