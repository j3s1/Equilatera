from django.urls import path, include
from rest_framework import routers
from . import views
from encuesta.views import RespuestasViewSet, OrganizacionesViewSet, PreguntasViewSet

router = routers.SimpleRouter()
router.register(r'preguntas', PreguntasViewSet)
router.register(r'respuestas', RespuestasViewSet)
router.register(r'organizaciones', OrganizacionesViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls))
]


