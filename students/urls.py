from django.urls import path
from . import views
from .api_views import StudentListCreateAPIView

urlpatterns = [
    path('', views.lista_studentow, name='lista_studentow'),
    #path('login/',        views.login,   name='login'),       # (opcjonalnie alias)
    #path('logout/',       views.logout,  name='logout'),      # (opcjonalnie alias)
    path('register/',     views.register,name='register'),

    path('student/dodaj/',        views.dodaj_student, name='dodaj_student'),
    path('student/edytuj/<int:student_id>/', views.edytuj_student, name='edytuj_student'),
    path('student/usun/<int:student_id>/',  views.usun_student,  name='usun_student'),
    path('profil/<int:student_id>/',       views.dodaj_lub_edytuj_profil, name='dodaj_edytuj_profil'),
    path('studenci/z_profilami/',  views.lista_studentow_z_profilami, name='lista_studentow_z_profilami'),
    path('studenci/bez_profilu/',  views.lista_studentow_bez_profilu, name='lista_studentow_bez_profilu'),

    path('studenci/z_projektami/',  views.lista_studentow_z_projektami, name='lista_studentow_z_projektami'),
    path('studenci/bez_projektow/', views.lista_studentow_bez_projektow, name='lista_studentow_bez_projektow'),
    path('projekt/dodaj/',           views.dodaj_projekt, name='dodaj_projekt'),

    path('kierunki/z_obsada/',       views.lista_kierunkow_z_obsada, name='lista_kierunkow_z_obsada'),
    path('kierunki/bez_obsady/',     views.lista_kierunkow_bez_obsady, name='lista_kierunkow_bez_obsady'),
    path('kierunek/dodaj/',          views.dodaj_kierunek, name='dodaj_kierunek'),
    path('kierunek/edytuj/<int:kierunek_id>/', views.edytuj_kierunek, name='edytuj_kierunek'),

    # API endpoint
    path('api/students/', StudentListCreateAPIView.as_view(), name='api_students'),
]
