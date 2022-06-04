from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class FormContatto(forms.Form):
    nome = forms.CharField(
        widget=forms.TextInput(
        attrs={"class": "form-control", "style":"width:500px;"}))
    cognome = forms.CharField(
        widget=forms.TextInput(
        attrs={"class": "form-control" , "style":"width:500px;"}))
    email = forms.EmailField(
        widget=forms.TextInput( 
        attrs={"class": "form-control" , "style":"width:500px;"}))
    contenuto = forms.CharField(
        widget=forms.Textarea(
        attrs={"placeholder": "Area Testuale! Scrivi pure!", "class": "form-control","style":"width:500px;" }),
        validators=[validators.MinLengthValidator(10)])

    def clean_contenuto(self):
        dati = self.cleaned_data["contenuto"]
        if "parola" in dati:
            raise ValidationError("Il contenuto inserito viole le norme del sito!")
        return dati
