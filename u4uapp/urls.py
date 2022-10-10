from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('universidades', views.universidades, name='universidades'),
    path('universidad/<int:universidad_id>', views.universidad, name='universidad'),
    path('carreras', views.carreras, name='carreras'),
    path('carrera/<int:carrera_id>', views.carrera, name='carrera'),
    path('carreraesp/<int:carreraesp_id>', views.carreraesp, name='carreraesp'),
    path('registrar_usuario', views.registrar_usuario, name='registrar_usuario'),
    path('iniciar_sesion', views.iniciar_sesion, name='iniciar_sesion'),
    path('cerrar_sesion', views.cerrar_sesion, name='cerrar_sesion'),
]
