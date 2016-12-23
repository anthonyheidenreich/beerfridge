from rest_framework import serializers
from beer.models import Beer, Brewery, Location, Glassware


class BrewerySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brewery
        fields = '__all__'


class LocationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'



class GlasswareSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Glassware
        fields = '__all__'


class BeerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Beer
        fields = '__all__'
