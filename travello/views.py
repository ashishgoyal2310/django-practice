from django.shortcuts import render
from travello.models import Destination
# Create your views here.


def index(request):

    # dest1 = Destination()
    # dest1.name = 'Mumbai'
    # dest1.des = ' Bollywood City ::: Hipee !!! '
    # dest1.price = 700
    # dest1.image = 'destination_1.jpg'
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = 'Delhi'
    # dest2.des = ' Country Capital City ::: Hipee !!! '
    # dest2.price = 555
    # dest2.image = 'destination_2.jpg'
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = 'Punjab'
    # dest3.des = ' Country Capital City ::: Hipee !!! '
    # dest3.price = 500
    # dest3.image = 'destination_3.jpg'
    # dest3.offer = False

    dests = Destination.objects.all()
    
    return render(request, 'index.html', {'dests':dests})
