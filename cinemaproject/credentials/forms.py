from django import forms

from cinemaapp.models import Movie


class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'category', 'description', 'release_date', 'actors', 'poster', 'trailer']