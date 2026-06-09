from django.urls import path
from .views import home,sobre,servicos

urlpatterns = [
    path('', home, name='home'),
    path('sobre/', sobre, name='sobre'),
    path('servicos/', servicos, name='servicos'),
]