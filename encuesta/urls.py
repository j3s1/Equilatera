from django.urls import path, include
from rest_framework import routers
from . import views
from encuesta.views import CuestionarioViewSet, RespuestasViewSet

router = routers.SimpleRouter()
router.register(r'cuestionario', CuestionarioViewSet)
router.register(r'respuestas', RespuestasViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls))
]

