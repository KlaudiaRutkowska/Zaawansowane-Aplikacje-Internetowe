from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Student, Profil
from .forms import StudentForm, ProfilForm

# Lista wszystkich studentów
def lista_studentow(request):
    students = Student.objects.all()
    return render(request, 'students/lista_studentow.html', {'students': students})

# Lista studentów z uzupełnionymi danymi profilowymi
def lista_studentow_z_profilami(request):
    students = Student.objects.filter(profil__isnull=False)
    return render(request, 'students/lista_studentow_z_profilami.html', {'students': students})

# Lista studentów bez danych profilowych
def lista_studentow_bez_profilu(request):
    students = Student.objects.filter(profil__isnull=True)
    return render(request, 'students/lista_studentow_bez_profilu.html', {'students': students})

# Dodawanie nowego studenta
def dodaj_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_studentow')
    else:
        form = StudentForm()
    return render(request, 'students/dodaj_student.html', {'form': form})

# Edycja danych studenta
def edytuj_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('lista_studentow')
    else:
        form = StudentForm(instance=student)
    return render(request, 'students/edytuj_student.html', {'form': form, 'student': student})

# Usuwanie studenta
def usun_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('lista_studentow')
    return render(request, 'students/usun_student.html', {'student': student})

# Dodawanie lub edycja danych profilowych studenta
def dodaj_lub_edytuj_profil(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    try:
        profil = student.profil
    except Profil.DoesNotExist:
        profil = None

    if request.method == 'POST':
        form = ProfilForm(request.POST, instance=profil)
        if form.is_valid():
            profil = form.save(commit=False)
            profil.student = student
            profil.save()
            return redirect('lista_studentow')
    else:
        form = ProfilForm(instance=profil)
    return render(request, 'students/dodaj_edytuj_profil.html', {'form': form, 'student': student})

