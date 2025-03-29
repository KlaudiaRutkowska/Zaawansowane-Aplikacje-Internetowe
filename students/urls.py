from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_studentow, name='lista_studentow'),
    path('student/dodaj/', views.dodaj_student, name='dodaj_student'),
    path('student/edytuj/<int:student_id>/', views.edytuj_student, name='edytuj_student'),
    path('student/usun/<int:student_id>/', views.usun_student, name='usun_student'),
    path('profil/<int:student_id>/', views.dodaj_lub_edytuj_profil, name='dodaj_edytuj_profil'),
    path('studenci/z_profilami/', views.lista_studentow_z_profilami, name='lista_studentow_z_profilami'),
    path('studenci/bez_profilu/', views.lista_studentow_bez_profilu, name='lista_studentow_bez_profilu'),
]
