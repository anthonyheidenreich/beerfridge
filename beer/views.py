from beer.constants import BEER_STYLES, GLASSWARE_STYLES
from beer.models import Beer, Brewery, Location, Glassware
from beer.serializers import BeerSerializer, BrewerySerializer, LocationSerializer, GlasswareSerializer
from django.shortcuts import render
from django.template import loader
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view()
def options(request):
    breweries = Brewery.objects.all()
    brewery_serializer = BrewerySerializer(breweries, context={'request': request}, many=True)
    locations = Location.objects.all()
    location_serializer = LocationSerializer(locations, context={'request': request}, many=True)
    return Response({
        'beer-styles': BEER_STYLES,
        'glassware-styles': GLASSWARE_STYLES,
        'breweries': brewery_serializer.data,
        'locations': location_serializer.data,
    })


def glassware(request):
    context = {
        'glasswares':  Glassware.objects.all
    }
    return render(request, 'glassware.html', context)


def index(request):
    context = { }
    return render(request, 'index.html', context)


def admin(request):
    context = { }
    return render(request, 'admin.html', context)


class BeerList(generics.ListCreateAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer


class BeerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Beer.objects.all()
    serializer_class = BeerSerializer


class BreweryList(generics.ListCreateAPIView):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer


class BreweryBeerList(generics.ListAPIView):
    serializer_class = BeerSerializer

    def get_queryset(self):
        return Beer.objects.filter(brewery=self.kwargs['pk'])


class BreweryGlasswareList(generics.ListAPIView):
    serializer_class = GlasswareSerializer

    def get_queryset(self):
        return Glassware.objects.filter(brewery=self.kwargs['pk'])


class BreweryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brewery.objects.all()
    serializer_class = BrewerySerializer


class LocationList(generics.ListCreateAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class LocationBeerList(generics.ListAPIView):
    serializer_class = BeerSerializer

    def get_queryset(self):
        return Beer.objects.filter(location=self.kwargs['pk'])


class LocationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class GlasswareList(generics.ListCreateAPIView):
    queryset = Glassware.objects.all()
    serializer_class = GlasswareSerializer


class GlasswareDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Glassware.objects.all()
    serializer_class = GlasswareSerializer
