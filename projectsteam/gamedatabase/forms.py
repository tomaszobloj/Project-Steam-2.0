from django import forms
from .models import GameDatabase

class GameDatabaseForm(forms.ModelForm):
    class Meta():
        model = GameDatabase
        fields = '__all__'