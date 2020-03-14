from django import forms
from django.contrib.auth.models import User

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



class PrivateForm(forms.Form):
    user = forms.CharField(label='Пользователь')

    def clean(self):
        super().clean()
        unknown_user = self.cleaned_data["user"]
        print(unknown_user)
        user = User.objects.get(username=unknown_user)
        if not user:
            raise forms.ValidationError('Пользователь' + '' + user + '' + 'не найден')
