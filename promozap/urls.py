from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('promo/', include('promo.urls')),
    # path('reset/', include('reset.urls'))
]