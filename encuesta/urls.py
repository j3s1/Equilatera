from django.urls import path, include
from rest_framework import routers
from . import views
from encuesta.views import RespuestasViewSet, OrganizacionesViewSet

router = routers.SimpleRouter()
router.register(r'respuestas', RespuestasViewSet)
router.register(r'organizacion', OrganizacionesViewSet)
urlpatterns = [
    path('', views.index, name='index'),
    path('api/', include(router.urls))
]


