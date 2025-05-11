
from django.urls import path
from .views import lista_estudiantes, detalle_estudiante, lista_profesores, detalle_profesor, index

app_name = "web1"

urlpatterns = [
    path('', index, name='index'),
    path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/<slug:slug>/', detalle_estudiante, name='detalle_estudiante'),
    path('profesores/', lista_profesores, name='lista_profesores'),
    path('profesores/<slug:slug>/', detalle_profesor, name='detalle_profesores'),

]