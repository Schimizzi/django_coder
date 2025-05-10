
from django.urls import path
from .views import lista_estudiantes, detalle_estudiante, lista_profesores, detalle_profesor

app_name = "web1"

urlpatterns = [
    path('estudiantes/', lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/<int:pk>/', detalle_estudiante, name='detalle_estudiante'),
    path('profesores/', lista_profesores, name='lista_profesores'),
    path('profesores/<int:pk>/', detalle_profesor, name='detalle_profesores'),
    #path('', index_view, name='index')

]