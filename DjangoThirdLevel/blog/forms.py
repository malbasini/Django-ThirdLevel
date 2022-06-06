from django import forms
from .models import BlogPostModel
from django.contrib.auth.models import User



class BlogPostModelForm(forms.ModelForm):
    
    class Meta():
        model = BlogPostModel
        fields = "__all__"
        
        
class FormRegistrazioneUser(forms.ModelForm):

    username = forms.CharField(widget=forms.TextInput())
    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    conferma_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username", "email", "password", "conferma_password"]

    def clean(self):
        """https://docs.djangoproject.com/en/dev/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other"""
        super().clean()
        password = self.cleaned_data.get("password")
        conferma_password = self.cleaned_data.get("conferma_password")
        if password != conferma_password:
           raise forms.ValidationError("Le password non combaciano!")
        return self.cleaned_data

        