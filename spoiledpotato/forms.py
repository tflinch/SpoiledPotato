from django import forms
from .models import Movie, Actor


from django_select2.forms import Select2MultipleWidget

class MovieForm(forms.ModelForm):
    actors = forms.ModelMultipleChoiceField(
        queryset=Actor.objects.all(),
        widget=Select2MultipleWidget,
        required=False
    )

    class Meta:
        model = Movie
        fields = ('title', 'actors', 'length', 'rating', 'preview_url')

class ActorForm(forms.ModelForm):
    
    class Meta:
        model = Actor
        fields = ('name', 'birthday', 'about', 'photo_url')


class SearchForm(forms.Form):
    query = forms.CharField(label='Search', max_length=100)
