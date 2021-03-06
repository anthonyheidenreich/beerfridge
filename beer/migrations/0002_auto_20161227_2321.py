# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-27 23:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('beer', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='beer',
            options={'ordering': ('name', 'brewery')},
        ),
        migrations.AlterModelOptions(
            name='brewery',
            options={'ordering': ('name',)},
        ),
        migrations.AlterModelOptions(
            name='glassware',
            options={'ordering': ('brewery', 'style')},
        ),
        migrations.AlterField(
            model_name='beer',
            name='style',
            field=models.CharField(choices=[('American-Style Wheat Wine Ale', 'American-Style Wheat Wine Ale'), ('American Wheat', 'American Wheat'), ('Belgian-Style Witbier', 'Belgian-Style Witbier'), ('Berliner-Style Weisse', 'Berliner-Style Weisse'), ('German-Style Dunkelweizen', 'German-Style Dunkelweizen'), ('German-Style Hefeweizen', 'German-Style Hefeweizen'), ('American Amber Ale', 'American Amber Ale'), ('English-Style Bitter', 'English-Style Bitter'), ('Blonde Ale', 'Blonde Ale'), ('English-Style Pale Ale (ESB)', 'English-Style Pale Ale (ESB)'), ('American Barley Wine', 'American Barley Wine'), ('American Strong Ale', 'American Strong Ale'), ('American Imperial Red Ale', 'American Imperial Red Ale'), ('British-Style Barley Wine Ale', 'British-Style Barley Wine Ale'), ('English-Style Old Ale', 'English-Style Old Ale'), ('Belgian-Style Blonde Ale', 'Belgian-Style Blonde Ale'), ('Belgian-Style Dubbel', 'Belgian-Style Dubbel'), ('Belgian-Style Golden Strong Ale', 'Belgian-Style Golden Strong Ale'), ('Belgian-Style Pale Ale', 'Belgian-Style Pale Ale'), ('Belgian-Style Quadrupel', 'Belgian-Style Quadrupel'), ('Belgian-Style Saison', 'Belgian-Style Saison'), ('Belgian-Style Tripel', 'Belgian-Style Tripel'), ('Scotch Ale/Wee Heavy', 'Scotch Ale/Wee Heavy'), ('Scottish-Style Ale', 'Scottish-Style Ale'), ('German-Style Bock', 'German-Style Bock'), ('German-Style Doppelbock', 'German-Style Doppelbock'), ('German-Style Maibock', 'German-Style Maibock'), ('German-Style Weizenbock', 'German-Style Weizenbock'), ('American Brown Ale', 'American Brown Ale'), ('English-Style Brown Ale', 'English-Style Brown Ale'), ('English-Style Mild', 'English-Style Mild'), ('American Brett', 'American Brett'), ('American Sour', 'American Sour'), ('Belgian-Style Flanders', 'Belgian-Style Flanders'), ('Belgian-Style Fruit Lambic', 'Belgian-Style Fruit Lambic'), ('Belgian-Style Lambic/Gueuze', 'Belgian-Style Lambic/Gueuze'), ('Sour Stout', 'Sour Stout'), ('Contemporary Gose', 'Contemporary Gose'), ('American Imperial Stout', 'American Imperial Stout'), ('Russian Imperial Stout', 'Russian Imperial Stout'), ('American Stout', 'American Stout'), ('English-Style Oatmeal Stout', 'English-Style Oatmeal Stout'), ('English-Style Sweet Stout (Milk Stout)', 'English-Style Sweet Stout (Milk Stout)'), ('Irish-Style Dry Stout', 'Irish-Style Dry Stout'), ('American IPA', 'American IPA'), ('Session IPA', 'Session IPA'), ('Brett IPA', 'Brett IPA'), ('English-Style IPA', 'English-Style IPA'), ('Imperial India Pale Ale', 'Imperial India Pale Ale'), ('American Lager', 'American Lager'), ('Inida Pale Lager', 'Inida Pale Lager'), ('Bohemian-Style Pilsener', 'Bohemian-Style Pilsener'), ('European-Style Export', 'European-Style Export'), ('German-Style Helles', 'German-Style Helles'), ('German-Style Pilsener', 'German-Style Pilsener'), ('American Amber Lager', 'American Amber Lager'), ('German-Style Dunkel', 'German-Style Dunkel'), ('German-Style Marzen / Oktoberfest', 'German-Style Marzen / Oktoberfest'), ('German-Style Schwarzbier', 'German-Style Schwarzbier'), ('Vienna-Style Lager', 'Vienna-Style Lager'), ('American Black Ale', 'American Black Ale'), ('Barrel-Aged Beer', 'Barrel-Aged Beer'), ('Chocolate Beer', 'Chocolate Beer'), ('Coffee Beer', 'Coffee Beer'), ('Fruit and Field Beer', 'Fruit and Field Beer'), ('Gluten Free', 'Gluten Free'), ('Herb and Spice Beer', 'Herb and Spice Beer'), ('Winter Warmer', 'Winter Warmer'), ('Honey Beer', 'Honey Beer'), ('Pumpkin Beer', 'Pumpkin Beer'), ('Rye Beer', 'Rye Beer'), ('Session Beer', 'Session Beer'), ('Smoke Beer', 'Smoke Beer'), ('Specialty Beer', 'Specialty Beer'), ('American Cream Ale', 'American Cream Ale'), ('French-Style Biere de Garde', 'French-Style Biere de Garde'), ('California Common', 'California Common'), ('German-Style Brown/Altbier', 'German-Style Brown/Altbier'), ('German-Style Kolsch', 'German-Style Kolsch'), ('Irish-Style Red', 'Irish-Style Red'), ('American Porter', 'American Porter'), ('American Imperial Porter', 'American Imperial Porter'), ('Baltic-Style Porter', 'Baltic-Style Porter'), ('English-Style Brown Porter', 'English-Style Brown Porter'), ('Robust Porter', 'Robust Porter'), ('Smoke Porter', 'Smoke Porter')], max_length=100),
        ),
        migrations.AlterField(
            model_name='brewery',
            name='city',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AlterField(
            model_name='glassware',
            name='style',
            field=models.CharField(choices=[('BOOT', 'Boot'), ('MUG', 'Mug'), ('GOBLET', 'Goblet'), ('FLUTE', 'Flute'), ('NOVELTY', 'Novelty'), ('PILSNER', 'Pilsner'), ('PINT', 'Pint'), ('STEIN', 'Stein'), ('TASTER', 'Taster'), ('TULIP', 'Tulip')], default='python', max_length=100),
        ),
    ]
