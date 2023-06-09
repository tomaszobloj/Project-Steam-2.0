from django.shortcuts import render,redirect
from .models import GameDatabase
from .forms import GameDatabaseForm

def index(request):
    gamedatabase = GameDatabase.objects.all()
    dict = {'gamedatabase':gamedatabase}
    return render(request, "index.html", dict)

def newgame(request):
    form = GameDatabaseForm()
    if request.method == 'POST':
        form = GameDatabaseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = GameDatabaseForm()
    return render(request, 'newgame.html',{"form":form})