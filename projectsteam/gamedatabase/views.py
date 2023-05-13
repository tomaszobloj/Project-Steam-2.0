from django.shortcuts import render
from .models import GameDatabase

def index(request):
    gamedatabase = GameDatabase.objects.all()
    dict = {'gamedatabase':gamedatabase}
    return render(request, "index.html", dict)
