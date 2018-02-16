from django import forms
from main.models import EmailAccess


class EmailAccessForm(forms.ModelForm):

    class Meta:
        model = EmailAccess
        fields = '__all__'
