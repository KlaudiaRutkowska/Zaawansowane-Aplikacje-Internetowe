from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Student,Profil,Projekt,Kierunek
from .forms import StudentForm,ProfilForm,ProjektForm,KierunekForm

# Lista wszystkich studentów
@login_required
def lista_studentow(request):
    students = Student.objects.all()
    return render(request, 'students/lista_studentow.html', {'students': students})

# Lista studentów z uzupełnionymi danymi profilowymi
@login_required
def lista_studentow_z_profilami(request):
    students = Student.objects.filter(profil__isnull=False)
    return render(request, 'students/lista_studentow_z_profilami.html', {'students': students})

# Lista studentów bez danych profilowych
@login_required
def lista_studentow_bez_profilu(request):
    students = Student.objects.filter(profil__isnull=True)
    return render(request, 'students/lista_studentow_bez_profilu.html', {'students': students})

# Dodawanie nowego studenta
@login_required
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
@login_required
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
@login_required
def usun_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('lista_studentow')
    return render(request, 'students/usun_student.html', {'student': student})

# Dodawanie lub edycja danych profilowych studenta
@login_required
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

@login_required
def lista_studentow_z_projektami(request):
    students = Student.objects.filter(projekty__isnull=False).distinct()
    return render(request,'students/lista_studentow_z_projektami.html',{'students':students})

@login_required
def lista_studentow_bez_projektow(request):
    students = Student.objects.filter(projekty__isnull=True)
    return render(request,'students/lista_studentow_bez_projektow.html',{'students':students})

@login_required
def dodaj_projekt(request):
    if request.method=='POST':
        form=ProjektForm(request.POST)
        if form.is_valid():
            p=form.save(commit=False)
            p.user=request.user
            p.save()
            return redirect('lista_studentow_z_projektami')
    else:
        form=ProjektForm()
    return render(request,'students/dodaj_projekt.html',{'form':form})

@login_required
def lista_kierunkow_z_obsada(request):
    kierunki = Kierunek.objects.filter(studenci__isnull=False).distinct()
    return render(request,'students/lista_kierunkow_z_obsada.html',{'kierunki':kierunki})

@login_required
def lista_kierunkow_bez_obsady(request):
    kierunki = Kierunek.objects.filter(studenci__isnull=True)
    return render(request,'students/lista_kierunkow_bez_obsady.html',{'kierunki':kierunki})

@login_required
def dodaj_kierunek(request):
    if request.method=='POST':
        form=KierunekForm(request.POST)
        if form.is_valid():
            k=form.save(commit=False)
            k.user=request.user
            k.save()
            form.save_m2m()
            return redirect('lista_kierunkow_z_obsada')
    else:
        form=KierunekForm()
    return render(request,'students/dodaj_kierunek.html',{'form':form})

@login_required
def edytuj_kierunek(request,kierunek_id):
    k=get_object_or_404(Kierunek,pk=kierunek_id)
    if request.method=='POST':
        form=KierunekForm(request.POST,instance=k)
        if form.is_valid():
            form.save()
            return redirect('lista_kierunkow_z_obsada')
    else:
        form=KierunekForm(instance=k)
    return render(request,'students/edytuj_kierunek.html',{'form':form,'kierunek':k})

def register(request):
    if request.method=="POST":
        form=UserCreationForm(request.POST)
        if form.is_valid():
            u=form.save()
            login(request,u)
            return redirect('lista_studentow')
    else:
        form=UserCreationForm()
    return render(request,'students/register.html',{'form':form})