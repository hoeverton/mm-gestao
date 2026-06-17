from django.shortcuts import render
from galeria.models import Foto
from django.http import HttpResponse
from django.contrib import messages


def home(request):

    fotos = Foto.objects.all()[:6]

    return render(
        request,
        'home.html',
        {
            'fotos': fotos
        }
    )
def sobre(request):
    return render(request, 'sobre.html')

def servicos(request):
    return render(request, 'servicos.html')



def contato(request):

    if request.method == 'POST':

        # Honeypot
        if request.POST.get('website'):
            messages.error(request, 'Bot detectado.')
            return render(request, 'contato.html')

        nome = request.POST.get('nome')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        mensagem = request.POST.get('mensagem')

        print("NOVO CONTATO")
        print(nome)
        print(email)
        print(telefone)
        print(mensagem)

        messages.success(
            request,
            'Mensagem enviada com sucesso!'
        )

    return render(request, 'contato.html')

def galeria(request):
    return render(request, 'galeria.html')

def galeria(request):
    fotos = Foto.objects.all()

    return render(
        request,
        'galeria.html',
        {
            'fotos': fotos
        }
    )

def robots_txt(request):
    content = """
User-agent: *
Allow: /

Sitemap: https://www.seudominio.com.br/sitemap.xml
"""
    return HttpResponse(content, content_type="text/plain")