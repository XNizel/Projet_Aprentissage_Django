from django.contrib import admin
from listings.models import Band
from listings.models import Listings

# Register your models here.

class BandAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

class ListingsAdmin(admin.ModelAdmin):  # nous insérons ces deux lignes..
    list_display = ('title', 'year_formed', 'type', 'band') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Band, BandAdmin) # nous modifions cett ligne, en ajoutant un deuxième argument
admin.site.register(Listings, ListingsAdmin) # nous modifions cett ligne, en ajoutant un deuxième argument
