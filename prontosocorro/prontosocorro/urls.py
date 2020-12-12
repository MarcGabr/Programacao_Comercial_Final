from django.contrib import admin
from django.urls import path, include
from prontosocorro.views import Autenticacao, sair


urlpatterns = [
    path('', Autenticacao.as_view(), name='index'),
    path('prontoatendimento/', include('prontoatendimento.urls')),
    path('admin/', admin.site.urls),
    path('', sair, name ='sair'),
    path('contas/', include('django.contrib.auth.urls')),
    #path('contas/', include('django.contrib.auth.urls')),
    # path('', index, name='index'),
    # path('/', index, name='index'),
    # re_path(r'/^(.*)$', index, name='index'),
    # re_path(r'^(.*)$', index, name='index'),
]

