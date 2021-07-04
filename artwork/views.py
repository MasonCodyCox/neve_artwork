from django.shortcuts import render, get_object_or_404
from .models import Artwork

# Create your views here.

def all_artwork(request):
    """ A view to show all items """

    artwork = Artwork.objects.all()

    context = {
        'artwork': artwork,
    }

    return render(request, 'artwork/artwork.html', context)


def artwork_detail(request, artwork_id):
    """ A view to show specific items """

    artwork = get_object_or_404(Artwork, pk=artwork_id)

    context = {
        'artwork': artwork,
    }

    return render(request, 'artwork/artwork_detail.html', context)
