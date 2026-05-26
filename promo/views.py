from django.shortcuts import redirect
from django.http import HttpResponse
from .models import AcessoPromo
from django.db import connection
from django.shortcuts import render

# from templates import index


LIMITE = 5
TEXT = 'Ola, quero garantir meu CASHBACK de R$230'

#PROMOÇAO VALIDA PARA 5 PESSOAS
def pagina_promo(request):

    total = AcessoPromo.objects.count()

    if total >= LIMITE:
         return HttpResponse("""
                <!DOCTYPE html>
                <html lang="pt-br">
                {% load static %}
                <head>

                    <meta charset="UTF-8">

                    <title>Promoção Encerrada</title>

                    <style>

                        body {
                            margin: 0;
                            padding: 0;
                            background: linear-gradient(135deg, #0f0f0f, #1a1a1a);
                            font-family: Arial, sans-serif;
                            display: flex;
                            justify-content: center;
                            align-items: center;
                            height: 100vh;
                            color: white;
                        }

                        .card {
                            background: #181818;
                            padding: 50px;
                            border-radius: 20px;
                            text-align: center;
                            width: 420px;
                            box-shadow:
                                0 0 30px rgba(255,0,0,0.2);
                        }

                        .emoji {
                            font-size: 60px;
                            margin-bottom: 20px;
                        }

                        .badge {
                            background: #2a2a2a;
                            color: #ff4d4d;
                            padding: 10px;
                            border-radius: 10px;
                            margin-bottom: 25px;
                            font-weight: bold;
                        }

                        h1 {
                            color: #ff4d4d;
                            font-size: 42px;
                            margin-bottom: 20px;
                        }

                        p {
                            color: #cfcfcf;
                            font-size: 18px;
                            line-height: 28px;
                        }

                    </style>

                </head>

                <body>

                    <div class="card">
                        <div class="badge">
                            PROMOÇÃO FINALIZADA
                        </div>

                        <h1>
                            Encerrada
                        </h1>

                        <p>
                            Todos os acessos promocionais já foram utilizados.
                        </p>

                    </div>

                </body>

                </html>

                """)
        # return render(request, 'templates/index.html',{
        #     'whatsapp': whatsapp
        # })


    AcessoPromo.objects.create(ip="usuario")

    # whatsapp = "https://wa.me/5516974002001?text=Ol%C3%A1%20vim%20pela%20promo%C3%A7%C3%A3o"
    whatsapp = f"https://wa.me/5516974002001?text={TEXT}"

    return HttpResponse(f"""
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="UTF-8">
                <style>

                    body {{
                        margin: 0;
                        padding: 0;
                        background: linear-gradient(135deg, #0f0f0f, #1a1a1a);
                        font-family:  Verdana, Geneva, Tahoma, sans-serif;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        color: white;
                    }}

                    .card {{
                        background: #181818;
                        padding: 50px;
                        border-radius: 20px;
                        text-align: center;
                        width: 600px;
                        box-shadow:
                            0 0 25px #1c90ea;
                    }}

                    h1 {{
                        font-size: 45px;
                        color: #25D366;
                        margin-bottom: 20px;
                    }}

                    p {{
                        color: #cfcfcf;
                        margin-bottom: 35px;
                        font-size: 25px;
                    }}

                    .btn {{
                        background: #25D366;
                        color: white;
                        border: none;
                        padding: 15px 30px;
                        border-radius: 12px;
                        font-size: 18px;
                        font-weight: bold;
                        cursor: pointer;
                        transition: 0.3s;
                    }}

                    .btn:hover {{
                        transform: scale(1.05);
                        background: #1ebe5d;
                    }}

                    .badge {{
                        background: #222;
                        padding: 10px;
                        border-radius: 10px;
                        margin-bottom: 20px;
                        color: #1c90ea;
                        font-weight: bold;
                        font-size: 50px;
                        font-family: 'Times New Roman', Times, serif;
                        text-decoration: underline;
                    }}

                </style>

            </head>

            <body>

                <div class="card">

                    <div class="badge">
                        PROMOÇÃO LIMITADA
                    </div>

                    <p>
                        Corra para garantir o CASHBACK clicando no botão abaixo.
                    </p>
                    <a href="{whatsapp}" target="_blank">

                        <button class="btn">
                            Abrir WhatsApp
                        </button>

                    </a>

                </div>

            </body>
            </html>
            """)
    # return render(request, 'templates/index.html',{
    #         'whatsapp': whatsapp
    #     })



def resetar(request):

    AcessoPromo.objects.all().delete()
    # connection.close()
    return HttpResponse("Acessos resetados!")