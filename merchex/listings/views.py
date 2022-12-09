from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactUsForm
from .models import Band
from .models import Listings


def band_list(request):
    bands = Band.objects.all()
    return render(request,
                  'bands/band_list.html',
                  {'bands': bands})


def band_detail(request, id):  # notez le paramètre id supplémentaire
    band = Band.objects.get(id=id)  # nous insérons cette ligne pour obtenir le Band avec cet id
    return render(request,
                  'bands/band_detail.html',
                  {'band': band})  # nous passons l'id au modèle


def about(request):
    return render(request,
                  'about/about.html')


def listings_list(request):
    listings = Listings.objects.all()
    return render(request,
                  'listings/listing_list.html',
                  {'listings': listings})


def listings_detail(request, id):
    listings = Listings.objects.get(id=id)
    return render(request,
                  'listings/listing_detail.html',
                  {'listing': listings})


def contact_us(request):
    print('La méthode de requête est : ', request.method)
    print('Les données POST sont : ', request.POST)

    if request.method == 'POST':
        # créer une instance de notre formulaire et le remplir avec les données POST
        form = ContactUsForm(request.POST)
    else:
        form = ContactUsForm()  # ajout d’un nouveau formulaire ici

    return render(request,
                  'listings/contact.html',
                  {'form': form})  # passe ce formulaire au gabarit
