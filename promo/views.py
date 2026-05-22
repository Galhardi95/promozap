from django.shortcuts import redirect
from django.http import HttpResponse
from .models import AcessoPromo
from django.db import connection


LIMITE = 1

#PROMOÇAO VALIDA PARA 5 PESSOAS
def pagina_promo(request):

    total = AcessoPromo.objects.count()

    if total >= LIMITE:
        return HttpResponse("""
            <h1>Promoção encerrada</h1>
            <p>Os acessos promocionais já foram utilizados.</p>
        """)

    AcessoPromo.objects.create(ip="usuario")

    whatsapp = "https://wa.me/5516974002001?text=Ol%C3%A1%20vim%20pela%20promo%C3%A7%C3%A3o"

    return HttpResponse(f"""
    <h2>Parabéns! Você conseguiu acessar</h2><br>
    <p>Clique no botao para garantir a promoção</p>

    <a href="{whatsapp}" target="_blank">
        <button style="
            padding: 15px;
            font-size: 20px;
            cursor: pointer;
        ">
            Garanta seu Desconto
        </button>
    </a>
""")
    # return HttpResponse("""
    #     <h2>Parabens voce conseguiu acessar a PROMOÇAO !!</h2>
    # """)



def resetar(request):

    AcessoPromo.objects.all().delete()
    # connection.close()

    return HttpResponse("Acessos resetados!")