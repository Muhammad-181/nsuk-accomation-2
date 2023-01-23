
from django import forms

from .models import Property, Location, Instituition
import django_filters







class PropertyFilter(django_filters.FilterSet):
    location = django_filters.ModelChoiceFilter(queryset=Location.objects.all())
    bedroom = django_filters.ChoiceFilter(choices=Property.BED_CHIOCES)
    bathroom = django_filters.ChoiceFilter(choices=Property.BATH_CHIOCES)
    min_price = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    max_price = django_filters.NumberFilter(field_name='price', lookup_expr='lte')
    class Meta:
        model = Property
        fields = ['location', 'bedroom', 'bathroom', 'min_price', 'max_price']



# class PropertyFilter(django_filters.FilterSet):
#     instituition = django_filters.ModelChoiceFilter(queryset=Instituition.objects.all())
#     location = django_filters.ModelChoiceFilter(queryset=Location.objects.all())
#     bedroom = django_filters.ChoiceFilter(choices=Property.BED_CHIOCES)
#     bathroom = django_filters.ChoiceFilter(choices=Property.BATH_CHIOCES)
#     min_price = django_filters.ChoiceFilter(choices=Property.PRICE_CHOICES, lookup_expr='gte')
#     max_price = django_filters.ChoiceFilter(choices=Property.PRICE_CHOICES, lookup_expr='lte')
#     class Meta:
#         model = Property
#         fields = ['instituition', 'location', 'bedroom', 'bathroom', 'min_price', 'max_price']   