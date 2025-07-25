from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control custom-input'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control custom-input'})
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control custom-input', 'rows': 4})
    )
