from django.urls import path
from . import views

urlpatterns = [
    # Cambia 'resolver_ruta' por 'resolver_todas_las_rutas'
    path('resolver/', views.resolver_todas_las_rutas, name='resolver_todas_las_rutas'),
]