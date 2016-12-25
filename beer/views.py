from beer.models import Beer, Brewery, Location, Glassware
from beer.serializers import BeerSerializer, BrewerySerializer, LocationSerializer, GlasswareSerializer
from rest_framework import generics
from django.template import loader
from django.shortcuts import render


def index(request):
    context = { }
    return render(request, 'index.html', context)


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
