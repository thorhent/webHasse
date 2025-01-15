from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('Gráficos/<ano>', views.graficos, name='graficos'),
    
]