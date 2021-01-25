"""app_enquetes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
]

'''
A função include() permite referenciar outras URLconfs. Qualquer lugar que o Django encontrar include(), irá recortar todas as partes da URL encontrada até aquele ponto e enviar a string restante para URLconf incluído para processamento posterior.
A idéia por trás do include() é facilitar plugar URLs.  Uma vez que polls está em sua própria URLconf (polls/urls.py), ele pode ser colocado depois de “/polls/”, ou depois de “/fun_polls/”, u depois de “/content/polls/”, ou qualquer outro início de caminho, e a aplicação ainda irá funcionar

Quando usar include() Deve-se sempre usar include() quando você incluir outros padrões de URL. admin.site.urls é a única exceção a isso.
'''