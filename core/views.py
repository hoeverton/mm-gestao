from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

from galeria.models import Foto
from contato.models import Contato


def home(request):
    fotos = Foto.objects.all()[:6]

    return render(
        request,
        "home.html",
        {
            "fotos": fotos
        }
    )


def sobre(request):
    return render(request, "sobre.html")


def servicos(request):
    return render(request, "servicos.html")


def galeria(request):
    fotos = Foto.objects.all()

    return render(
        request,
        "galeria.html",
        {
            "fotos": fotos
        }
    )


def contato(request):

    if request.method == "POST":

        # Honeypot contra bots
        if request.POST.get("website"):
            messages.error(request, "Bot detectado.")
            return render(request, "contato.html")

        nome = request.POST.get("nome")
        email = request.POST.get("email")
        telefone = request.POST.get("telefone")
        mensagem = request.POST.get("mensagem")

        # Salva no banco
        Contato.objects.create(
            nome=nome,
            email=email,
            telefone=telefone,
            mensagem=mensagem,
        )

        corpo = f"""
Novo contato recebido pelo site M&M Gestão em Saúde

Nome: {nome}
Email: {email}
Telefone: {telefone}

Mensagem:

{mensagem}
"""

        try:

            # Email para a empresa
            send_mail(
                subject=f"Novo contato do site - {nome}",
                message=corpo,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False,
            )

            # Email automático para quem entrou em contato
            send_mail(
                subject="Recebemos sua mensagem",
                message=f"""
Olá {nome},

Recebemos sua mensagem com sucesso.

Nossa equipe entrará em contato o mais breve possível.

Obrigado pela confiança.

Atenciosamente,

M&M Gestão em Saúde
""",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False,
            )

        except Exception:

            messages.error(
                request,
                "Sua mensagem foi salva, porém ocorreu um problema ao enviar os e-mails."
            )

            return redirect("obrigado")

        messages.success(
            request,
            "Mensagem enviada com sucesso!"
        )

        return redirect("obrigado")

    return render(request, "contato.html")


def robots_txt(request):

    content = """
User-agent: *
Allow: /

Sitemap: https://www.mmgestaosaude.com.br/sitemap.xml
"""

    return HttpResponse(
        content,
        content_type="text/plain"
    )


def obrigado(request):
    return render(request, "obrigado.html")