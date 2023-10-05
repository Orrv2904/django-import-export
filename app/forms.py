from django import forms
from .models import Person


class PersonForm(forms.Form):
    class meta:
        model = Person
        fields = '__all__'