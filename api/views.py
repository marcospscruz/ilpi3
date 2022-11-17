from django.shortcuts import render

# Create your views here.

from betel.models import Hospede, Fator_de_Risco_Social, Familiar, Equipe, Anotacao_de_Enfermagem, Sinais_Vitais, Controle_de_Dextro, Evolucao, Medicacao, Prescricao, Enfermidade, Ficha_de_Avaliacao, Item, Estoque
from rest_framework import viewsets 
from rest_framework import permissions 
from api.serializers import HospedeSerializer, Fator_de_Risco_SocialSerializer, FamiliarSerializer, EquipeSerializer, Anotacao_de_EnfermagemSerializer, Sinais_VitaisSerializer, Controle_de_DextroSerializer, EvolucaoSerializer, MedicacaoSerializer, PrescricaoSerializer, EnfermidadeSerializer, Ficha_de_AvaliacaoSerializer, ItemSerializer, EstoqueSerializer

class HospedeViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar Hóspedes. 
    """ 
    queryset = Hospede.objects.all()
    serializer_class = HospedeSerializer 
    permission_classes = [permissions.IsAuthenticated]
	
class Fator_de_Risco_SocialViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar Fatores de risco social. 
    """ 
    queryset = Fator_de_Risco_Social.objects.all()
    serializer_class = Fator_de_Risco_SocialSerializer 
    permission_classes = [permissions.IsAuthenticated]
	
class FamiliarViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar Familiares. 
    """ 
    queryset = Familiar.objects.all()
    serializer_class = FamiliarSerializer 
    permission_classes = [permissions.IsAuthenticated]

class EquipeViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar membros da equipe. 
    """ 
    queryset = Equipe.objects.all()
    serializer_class = EquipeSerializer 
    permission_classes = [permissions.IsAuthenticated]
	
class Anotacao_de_EnfermagemViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar as anotações de enfermagem. 
    """ 
    queryset = Anotacao_de_Enfermagem.objects.all()
    serializer_class = Anotacao_de_EnfermagemSerializer 
    permission_classes = [permissions.IsAuthenticated]
    
class Sinais_VitaisViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar Sinais Vitais. 
    """ 
    queryset = Sinais_Vitais.objects.all()
    serializer_class = Sinais_VitaisSerializer 
    permission_classes = [permissions.IsAuthenticated]
	
class Controle_de_DextroViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar o controle de dextro. 
    """ 
    queryset = Controle_de_Dextro.objects.all()
    serializer_class = Controle_de_DextroSerializer 
    permission_classes = [permissions.IsAuthenticated]
	
class EvolucaoViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar as evoluções dos hóspedes 
    """ 
    queryset = Evolucao.objects.all()
    serializer_class = EvolucaoSerializer 
    permission_classes = [permissions.IsAuthenticated]
	
class MedicacaoViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar as evoluções dos hóspedes 
    """ 
    queryset = Medicacao.objects.all()
    serializer_class = MedicacaoSerializer 
    permission_classes = [permissions.IsAuthenticated]
	
class PrescricaoViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar as prescrições dos hóspedes 
    """ 
    queryset = Prescricao.objects.all()
    serializer_class = PrescricaoSerializer 
    permission_classes = [permissions.IsAuthenticated]
	
class EnfermidadeViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar as enfermidades cadastradas 
    """ 
    queryset = Enfermidade.objects.all()
    serializer_class = EnfermidadeSerializer 
    permission_classes = [permissions.IsAuthenticated]
	
class Ficha_de_AvaliacaoViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar as fichas de avaliação dos hóspedes 
    """ 
    queryset = Ficha_de_Avaliacao.objects.all()
    serializer_class = Ficha_de_AvaliacaoSerializer
    permission_classes = [permissions.IsAuthenticated]
	
class ItemViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar os itens em estoque 
    """ 
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
	
class EstoqueViewSet(viewsets.ModelViewSet): 
    """ 
    API que permite visualizar o estoque por hóspede
    """ 
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
    permission_classes = [permissions.IsAuthenticated]