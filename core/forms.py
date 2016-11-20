from django import forms
from .models import Game, Image

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ('title','publication_date','developer','game_type','image',)

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('title','image',)
