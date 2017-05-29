from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from beer import views

urlpatterns = [
    url(r'^old$', views.index, name='index'),
    url(r'^admin$', views.admin, name='admin'),
    url(r'^$', views.glassware, name='glassware'),
    url(r'^v1/beers/?$', views.BeerList.as_view(), name='beer-list'),
    url(r'^v1/beers/(?P<pk>[0-9]+)/?$', views.BeerDetail.as_view(), name='beer-detail'),
    url(r'^v1/breweries/?$', views.BreweryList.as_view(), name='brewery-list'),
    url(r'^v1/breweries/(?P<pk>[0-9a-zA-Z-]+)/?$', views.BreweryDetail.as_view(), name='brewery-detail'),
    url(r'^v1/breweries/(?P<pk>[0-9a-zA-Z-]+)/beers/?$', views.BreweryBeerList.as_view(), name='brewery-beer-list'),
    url(r'^v1/breweries/(?P<pk>[0-9a-zA-Z-]+)/glasswares/?$', views.BreweryGlasswareList.as_view(), name='brewery-glassware-list'),
    url(r'^v1/locations/?$', views.LocationList.as_view(), name='location-list'),
    url(r'^v1/locations/(?P<pk>[0-9a-zA-Z-]+)/?$', views.LocationDetail.as_view(), name='location-detail'),
    url(r'^v1/locations/(?P<pk>[0-9a-zA-Z-]+)/beers/?$', views.LocationBeerList.as_view(), name='location-beer-list'),
    url(r'^v1/glasswares/?$', views.GlasswareList.as_view(), name='glassware-list'),
    url(r'^v1/glasswares/(?P<pk>[0-9]+)/?$', views.GlasswareDetail.as_view(), name='glassware-detail'),
    url(r'^v1/options/?$', views.options, name='option-list'),
]
