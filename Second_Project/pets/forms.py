from django import forms
from .models import Pet, Comment
from .models import AdoptionRequest

class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        fields = ['name', 'age', 'breed', 'category', 'description', 'image', 'available']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'age': forms.NumberInput(attrs={'class': 'form-control custom-input'}),
            'breed': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'category': forms.Select(attrs={'class': 'form-select custom-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control custom-input', 'rows': 4}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control custom-input'}),
            'available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'text']


class AdoptionRequestForm(forms.ModelForm):
    class Meta:
        model = AdoptionRequest
        fields = ['name', 'email', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'email': forms.EmailInput(attrs={'class': 'form-control custom-input'}),
            'phone': forms.TextInput(attrs={'class': 'form-control custom-input'}),
            'message': forms.Textarea(attrs={'class': 'form-control custom-input', 'rows': 4}),
        }