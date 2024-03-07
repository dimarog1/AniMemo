from .models import AnimePreview
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class AnimePreviewForm(ModelForm):
    class Meta:
        model = AnimePreview
        fields = ['russian_title']

        widgets = {
            'russian_title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Название аниме...',
                'aria-describedby': 'button-addon2',
                'id': 'animeInput',
                'type': 'text'
            })
        }
