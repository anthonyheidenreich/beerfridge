from rest_framework import serializers
from beer.models import Beer, Brewery, Location, Glassware


class BrewerySerializer(serializers.ModelSerializer):
    beers = serializers.HyperlinkedIdentityField(view_name='brewery-beer-list')
    glasswares = serializers.HyperlinkedIdentityField(view_name='brewery-glassware-list')

    class Meta:
        model = Brewery
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    beers = serializers.HyperlinkedIdentityField(view_name='location-beer-list')

    class Meta:
        model = Location
        fields = '__all__'



class GlasswareSerializer(serializers.ModelSerializer):
    brewery_url = serializers.HyperlinkedIdentityField(view_name='brewery-detail')

    class Meta:
        model = Glassware
        fields = '__all__'


class BeerSerializer(serializers.ModelSerializer):
    brewery_url = serializers.HyperlinkedIdentityField(view_name='brewery-detail')
    location_url = serializers.HyperlinkedIdentityField(view_name='location-detail')

    class Meta:
        model = Beer
        fields = '__all__'
