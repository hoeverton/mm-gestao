from django.urls import path
from .views import home,sobre,servicos, contato, galeria,robots_txt, obrigado

urlpatterns = [
    path('', home, name='home'),
    path('sobre/', sobre, name='sobre'),
    path('servicos/', servicos, name='servicos'),
    path('contato/', contato, name='contato'),
    path('galeria/', galeria, name='galeria'),
    path('robots.txt', robots_txt, name='robots_txt'),
    path('obrigado/', obrigado, name='obrigado'),
]