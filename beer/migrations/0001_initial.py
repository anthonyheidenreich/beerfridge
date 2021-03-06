# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-22 22:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('style', models.CharField(choices=[('American-Style Wheat Wine Ale', 'American-Style Wheat Wine Ale'), ('American Wheat', 'American Wheat'), ('Belgian-Style Witbier', 'Belgian-Style Witbier'), ('Berliner-Style Weisse', 'Berliner-Style Weisse'), ('German-Style Dunkelweizen', 'German-Style Dunkelweizen'), ('German-Style Hefeweizen', 'German-Style Hefeweizen'), ('American Black Ale', 'American Black Ale'), ('Barrel-Aged Beer', 'Barrel-Aged Beer'), ('Chocolate Beer', 'Chocolate Beer'), ('Coffee Beer', 'Coffee Beer'), ('Fruit and Field Beer', 'Fruit and Field Beer'), ('Gluten Free', 'Gluten Free'), ('Herb and Spice Beer', 'Herb and Spice Beer'), ('Honey Beer', 'Honey Beer'), ('Pumpkin Beer', 'Pumpkin Beer'), ('Rye Beer', 'Rye Beer'), ('Session Beer', 'Session Beer'), ('Smoke Beer', 'Smoke Beer'), ('Specialty Beer', 'Specialty Beer'), ('American IPA', 'American IPA'), ('English-Style IPA', 'English-Style IPA'), ('Imperial India Pale Ale', 'Imperial India Pale Ale'), ('American Imperial Stout', 'American Imperial Stout'), ('American Stout', 'American Stout'), ('English-Style Oatmeal Stout', 'English-Style Oatmeal Stout'), ('English-Style Sweet Stout (Milk Stout)', 'English-Style Sweet Stout (Milk Stout)'), ('Irish-Style Dry Stout', 'Irish-Style Dry Stout'), ('American Brown Ale', 'American Brown Ale'), ('English-Style Brown Ale', 'English-Style Brown Ale'), ('English-Style Mild', 'English-Style Mild'), ('American Cream Ale', 'American Cream Ale'), ('French-Style Biere de Garde', 'French-Style Biere de Garde'), ('California Common', 'California Common'), ('German-Style Brown/Altbier', 'German-Style Brown/Altbier'), ('German-Style Kolsch', 'German-Style Kolsch'), ('Irish-Style Red', 'Irish-Style Red'), ('American Amber Lager', 'American Amber Lager'), ('German-Style Dunkel', 'German-Style Dunkel'), ('German-Style Marzen / Oktoberfest', 'German-Style Marzen / Oktoberfest'), ('German-Style Schwarzbier', 'German-Style Schwarzbier'), ('Vienna-Style Lager', 'Vienna-Style Lager'), ('American Barley Wine', 'American Barley Wine'), ('American Imperial Red Ale', 'American Imperial Red Ale'), ('British-Style Barley Wine Ale', 'British-Style Barley Wine Ale'), ('English-Style Old Ale', 'English-Style Old Ale'), ('Scotch Ale/Wee Heavy', 'Scotch Ale/Wee Heavy'), ('Scottish-Style Ale', 'Scottish-Style Ale'), ('American Porter', 'American Porter'), ('American Imperial Porter', 'American Imperial Porter'), ('Baltic-Style Porter', 'Baltic-Style Porter'), ('English-Style Brown Porter', 'English-Style Brown Porter'), ('Robust Porter', 'Robust Porter'), ('Smoke Porter', 'Smoke Porter'), ('American Lager', 'American Lager'), ('Bohemian-Style Pilsener', 'Bohemian-Style Pilsener'), ('European-Style Export', 'European-Style Export'), ('German-Style Helles', 'German-Style Helles'), ('German-Style Pilsener', 'German-Style Pilsener'), ('American Amber Ale', 'American Amber Ale'), ('American Pale Ale', 'American Pale Ale'), ('English-Style Bitter', 'English-Style Bitter'), ('Blonde Ale', 'Blonde Ale'), ('English-Style Pale Ale (ESB)', 'English-Style Pale Ale (ESB)'), ('American Brett', 'American Brett'), ('American Sour', 'American Sour'), ('Belgian-Style Flanders', 'Belgian-Style Flanders'), ('Belgian-Style Fruit Lambic', 'Belgian-Style Fruit Lambic'), ('Belgian-Style Lambic/Gueuze', 'Belgian-Style Lambic/Gueuze'), ('Contemporary Gose', 'Contemporary Gose'), ('Belgian-Style Blonde Ale', 'Belgian-Style Blonde Ale'), ('Belgian-Style Dubbel', 'Belgian-Style Dubbel'), ('Belgian-Style Golden Strong Ale', 'Belgian-Style Golden Strong Ale'), ('Belgian-Style Pale Ale', 'Belgian-Style Pale Ale'), ('Belgian-Style Quadrupel', 'Belgian-Style Quadrupel'), ('Belgian-Style Saison', 'Belgian-Style Saison'), ('Belgian-Style Tripel', 'Belgian-Style Tripel'), ('German-Style Bock', 'German-Style Bock'), ('German-Style Doppelbock', 'German-Style Doppelbock'), ('German-Style Maibock', 'German-Style Maibock'), ('German-Style Weizenbock', 'German-Style Weizenbock')], max_length=100)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Brewery',
            fields=[
                ('id', models.SlugField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Glassware',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('style', models.CharField(choices=[('BOOTS', 'Boots'), ('MUGS', 'Mugs'), ('GOBLETS', 'Goblets'), ('FLUTES', 'Flutes'), ('NOVELTY', 'Novelty'), ('PILSNERS', 'Pilsners'), ('PINTS', 'Pints'), ('STEINS', 'Steins'), ('TASTER', 'Taster'), ('TULIPS', 'Tulips')], default='python', max_length=100)),
                ('description', models.CharField(max_length=201)),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brewery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='beer.Brewery')),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.SlugField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.AddField(
            model_name='beer',
            name='brewery',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.Brewery'),
        ),
        migrations.AddField(
            model_name='beer',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='beer.Location'),
        ),
    ]
