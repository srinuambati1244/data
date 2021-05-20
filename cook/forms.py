from django import forms
from .models import UserData


class UserDataForm(forms.Form):
    class Meta:
        model = UserData
        fields = '__all__'
