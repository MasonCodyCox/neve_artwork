from django.shortcuts import render
from .models import Artwork

# Create your views here.

def all_artwork(request):
    """ A view to show all items """

    artwork = Artwork.objects.all()

    context = {
        'artwork': artwork,
    }

    return render(request, 'artwork/artwork.html', context)
