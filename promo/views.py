from django.shortcuts import redirect
from django.http import HttpResponse
from .models import AcessoPromo

LIMITE = 1
TEXT = 'Ola, acessei o link e sou um dos ganhadores da promocao!!'

def pagina_promo(request):

    ip = request.META.get('REMOTE_ADDR')

    total = AcessoPromo.objects.count()

    if total >= LIMITE:
        return HttpResponse("""
            <h1>Promoção encerrada</h1>
            <p>Os acessos promocionais já foram utilizados.</p>
        """)

    ja_existe = AcessoPromo.objects.filter(ip=ip).exists()

    if not ja_existe:
        AcessoPromo.objects.create(ip=ip)

    whatsapp = "https://wa.me/5516996268400?text=Ol%C3%A1%20vim%20pela%20promo%C3%A7%C3%A3o"

    return redirect(whatsapp)


def resetar(request):

    AcessoPromo.objects.all().delete()

    return HttpResponse("Acessos resetados!")