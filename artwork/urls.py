from django.urls import path, include
from . import views

urlpatterns = [
    path('',  views.all_artwork, name='artwork'),
    path('<artwork_id>',  views.artwork_detail, name='artwork_detail')
]
