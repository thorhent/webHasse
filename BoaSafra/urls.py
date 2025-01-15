from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('Gráficos/<ano>/<intervalo>', views.graficos, name='graficos'),
    
]