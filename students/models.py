from django.db import models

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
