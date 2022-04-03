from django.contrib import admin
from django.urls import path

from usuarios.views import index
from visitantes.views import registrar_visitante

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",  # path da URL
        index,  # função a ser chamada
        name="index",  # nome da URL
    ),

    path(
        "registrar-visitante/",
        registrar_visitante,
        name="registrar_visitante",

    )
]
