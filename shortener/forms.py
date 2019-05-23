from .models import *
from django import forms


class urlForm(forms.ModelForm):
    original_url = forms.CharField(label='Your URL', widget=forms.CharField)

    class Meta:
        model = Urls
        fields = ('originalUrl',)
