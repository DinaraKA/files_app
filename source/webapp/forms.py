from django import forms
from webapp.models import File


class SimpleSearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False, label="Поиск")


class FileForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file', 'access']


class FileAnonymousForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file']
