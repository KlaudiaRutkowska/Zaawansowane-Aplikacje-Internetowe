from django.db import models
from django.contrib.auth.models import User

class Student(models.Model):
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    indeks = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.imie} {self.nazwisko} ({self.indeks})"

class Profil(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='profil')
    adres = models.CharField(max_length=200)
    telefon = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return f"Profil: {self.student}"

class Projekt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='projekty')
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='projekty')
    temat = models.CharField(max_length=200)
    ocena = models.PositiveSmallIntegerField(choices=[(2,'2'),(3,'3'),(4,'4'),(5,'5')])
    def __str__(self):
        return f"{self.temat} - {self.ocena}"

class Kierunek(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='kierunki')
    nazwa = models.CharField(max_length=200)
    opis = models.TextField()
    studenci = models.ManyToManyField(Student, related_name='kierunki')
    def __str__(self):
        return self.nazwa