from django.shortcuts import render
from visitantes.models import Visitante


def index(request):
    todos_visitantes = Visitante.objects.all()

    visitantes_aguardando = todos_visitantes.filter(status='AGUARDANDO')
    visitantes_em_visita = todos_visitantes.filter(status='EM_VISITA')
    visitantes_finalizados = todos_visitantes.filter(status='FINALIZADO')

    context = {
        "nome_pagina": "Início da dashboard",
        "todos_visitantes": todos_visitantes,
        "visitantes_aguardando": visitantes_aguardando.count(),
        "visitantes_em_visita": visitantes_em_visita.count(),
        "visitantes_finalizados": visitantes_finalizados.count(),
    }
    return render(request, "index.html", context)
