from rest_framework import serializers
from cscapp.models import *

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Countries
        # fields = '__all__'
        fields = ['id', 'name', 'iso2']


class StateSerializer(serializers.ModelSerializer):
    # country_name = serializers.CharField(source='country', read_only=True)
    class Meta:
        model = States
        # fields = ['id', 'name', 'country', 'country_name', 'country_code']
        fields = ['id', 'name']


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['id', 'name']