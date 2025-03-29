from django import forms
from .models import Student, Profil

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['imie', 'nazwisko', 'indeks']

class ProfilForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['adres', 'telefon', 'email']
