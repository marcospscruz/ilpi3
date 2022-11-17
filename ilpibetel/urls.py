"""ilpibetel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.conf.urls import include
from rest_framework import routers 
from api import views  

router = routers.DefaultRouter() 

router.register(r'hospedes', views.HospedeViewSet)
router.register(r'fatoresderisco', views.Fator_de_Risco_SocialViewSet) 
router.register(r'familiares', views.FamiliarViewSet)
router.register(r'equipe', views.EquipeViewSet)
router.register(r'anotacoes', views.Anotacao_de_EnfermagemViewSet) 
router.register(r'sinaisvitais', views.Sinais_VitaisViewSet) 
router.register(r'dextro', views.Controle_de_DextroViewSet) 
router.register(r'evolucoes', views.EvolucaoViewSet)
router.register(r'medicacoes', views.MedicacaoViewSet)
router.register(r'prescricoes', views.PrescricaoViewSet)
router.register(r'enfermidades', views.EnfermidadeViewSet)
router.register(r'fichasdeavaliacao', views.Ficha_de_AvaliacaoViewSet)
router.register(r'itens', views.ItemViewSet)    
router.register(r'estoque', views.EstoqueViewSet) 

urlpatterns = [
    path("admin/", admin.site.urls),
]

urlpatterns += [ 
    path('betel/', include('betel.urls')), 
	path('accounts/', include('django.contrib.auth.urls')),
]

from django.views.generic import RedirectView

urlpatterns += [ 
    path('', RedirectView.as_view(url='/betel/')), 
]

urlpatterns += [ 
    path('', include(router.urls)), 
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')) 
]   

from django.conf import settings 
from django.conf.urls.static import static 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) 
