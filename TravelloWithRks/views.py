from django.shortcuts import render
from .models import Destination
# Create your views here.

def index(request):

    #Setting data manually
    # dest1 = Destination()
    # dest1.name = "Mumbai"
    # dest1.desc = "The City Of Dream"
    # dest1.img = 'destination_1.jpg'
    # dest1.price = "700"
    # dest1.offer = False

    # dest2 = Destination()
    # dest2.name = "BodhGaya"
    # dest2.desc = "The Land Of Peace"
    # dest2.img = 'destination_2.jpg'
    # dest2.price = "400"
    # dest2.offer = True

    # dest3 = Destination()
    # dest3.name = "Kolkata"
    # dest3.desc = "The City Of Joy"
    # dest3.img = 'destination_3.jpg'
    # dest3.price = "450"
    # dest3.offer = True

    # dest4 = Destination()
    # dest4.name = "Delhi"
    # dest4.desc = "The Capital Of India"
    # dest4.img = 'destination_4.jpg'
    # dest4.price = "500"
    # dest4.offer = False


    # dests = [dest1, dest2, dest3, dest4]

    #fetching data from database dynamically
    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})
