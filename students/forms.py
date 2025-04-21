from django import forms
from .models import Student, Profil, Projekt, Kierunek

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['imie', 'nazwisko', 'indeks']

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['adres', 'telefon', 'email']

class ProjektForm(forms.ModelForm):
    class Meta:
        model = Projekt
        fields = ['student','temat','ocena']

class KierunekForm(forms.ModelForm):
    class Meta:
        model = Kierunek
        fields = ['nazwa','opis','studenci']

