from django import forms
from .models import Pet, Comment


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'age', 'breed', 'category', 'description', 'image', 'available']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']
