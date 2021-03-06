from django.db import models
from beer.constants import BEER_STYLE_CHOICES, GLASSWARE_STYLES


class Location(models.Model):
    id = models.SlugField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('id',)


class Brewery(models.Model):
    id = models.SlugField(primary_key=True)
    name = models.CharField(max_length=100, blank=False)
    logo = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)


class Beer(models.Model):
    name = models.CharField(max_length=200, blank=False)
    brewery = models.ForeignKey(Brewery, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    style = models.CharField(choices=BEER_STYLE_CHOICES, max_length=100)
    image = models.CharField(max_length=255, blank=True)
    quantity = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name', 'brewery')


class Glassware(models.Model):
    brewery = models.CharField(max_length=255, null=False)
    style = models.CharField(choices=GLASSWARE_STYLES, default='python', max_length=100)
    image = models.CharField(max_length=255, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('brewery', 'style')
