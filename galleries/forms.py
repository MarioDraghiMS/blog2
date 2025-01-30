from django import forms
from .models import Gallery, Photo

class GalleryForm(forms.ModelForm):
    class Meta:
        model = Gallery
        fields = ['name', 'description']

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['image', 'description']