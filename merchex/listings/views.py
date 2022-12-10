from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactUsForm
from .models import Band
from .models import Listings
from listings.forms import ContactUsForm


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

        if form.is_valid():
            send_mail(
                subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
                message=form.cleaned_data['message'],
                from_email=form.cleaned_data['email'],
                recipient_list=['admin@merchex.xyz'],
            )
            return redirect('email-sent')  # ajoutez cette instruction de retour

        # si le formulaire n'est pas valide, nous laissons l'exécution continuer jusqu'au return
        # ci-dessous et afficher à nouveau le formulaire (avec des erreurs).

    else:
        form = ContactUsForm()  # ajout d’un nouveau formulaire ici

    return render(request,
                  'listings/contact.html',
                  {'form': form})  # passe ce formulaire au gabarit


def email_sent(request):
    return render(request,
                  'email_sent/email_sent.html')
