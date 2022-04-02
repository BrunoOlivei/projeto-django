from django.contrib import admin
from django.urls import path

from usuarios.views import index

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "",  # path da URL
        index,  # função a ser chamada
        name="index",  # nome da URL
    )
]
