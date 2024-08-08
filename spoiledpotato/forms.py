from django import forms
from .models import Movie, Actor


class MovieForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title','actors' ,'length', 'rating', 'preview_url')

