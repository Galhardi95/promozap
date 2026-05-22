from django.urls import path
from .views import pagina_promo, resetar

urlpatterns = [
    path('', pagina_promo),
    path('reset/', resetar)
]