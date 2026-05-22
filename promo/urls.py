from django.urls import path
from .views import pagina_promo

urlpatterns = [
    path('', pagina_promo),
]