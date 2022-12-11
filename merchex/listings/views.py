from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import ContactUsForm
from .models import Band
from .models import Listings
from listings.forms import BandForm, ListingForm, ContactUsForm


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


def band_create(request):
    if request.method == 'POST':
        form = BandForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            band = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('band-detail', band.id)

    else:
        form = BandForm()

    return render(request,
                  'bands/band_create.html',
                  {'form': form})


def band_change(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            # mettre à jour le groupe existant dans la base de données
            form.save()
            # rediriger vers la page détaillée du groupe que nous venons de mettre à jour
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request,
                  'bands/band_change.html',
                  {'form': form})


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


def listing_create(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            # créer une nouvelle « Band » et la sauvegarder dans la db
            listing = form.save()
            # redirige vers la page de détail du groupe que nous venons de créer
            # nous pouvons fournir les arguments du motif url comme arguments à la fonction de redirection
            return redirect('listing-detail', listing.id)

    else:
        form = ListingForm()

    return render(request,
                  'listings/listing_create.html',
                  {'form': form})


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
