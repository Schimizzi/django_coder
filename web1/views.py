
from django.shortcuts import render, get_object_or_404
from .models import Estudiante, Profesor, Curso, Entregable

def index(request):
    return render(request, 'web1/index.html')

def lista_estudiantes(request):
    estudiantes = Estudiante.objects.all()
    return render(request, 'web1/estudiantes_list.html', {'estudiantes': estudiantes})

def detalle_estudiante(request, slug): 
    estudiante = get_object_or_404(Estudiante, slug=slug)
    return render(request, 'web1/estudiante_detail.html', {'estudiante': estudiante})

def lista_profesores(request):
    profesores = Profesor.objects.all()
    return render(request, 'web1/profesores_list.html', {'profesores': profesores})

def detalle_profesor(request, slug):
    profesor = get_object_or_404(Profesor, slug=slug)
    return render(request, 'web1/profesor_detail.html', {'profesor': profesor})

