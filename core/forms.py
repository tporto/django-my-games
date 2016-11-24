from django import forms
from .models import Photo, Game

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('title','file',)

class GameForm(forms.ModelForm):
    image = forms.ModelChoiceField(queryset=Photo.objects.filter(cover=1).order_by('title'),empty_label="Select an image",label='Image:',)
    class Meta:
        model = Game
        fields = ('title','publication_date','developer','game_type','image',)
