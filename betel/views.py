from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required 
from django.utils.decorators import method_decorator  
from betel.models import Hospede, Familiar, Equipe, Anotacao_de_Enfermagem, Sinais_Vitais, Controle_de_Dextro, Evolucao, Medicacao, Prescricao, Ficha_de_Avaliacao, Item, Estoque 
from django.urls import reverse_lazy 

# Create your views here.


def index(request):
    '''Função view para a página index'''
    return render(request, 'index.html')

@method_decorator(login_required, name='dispatch') 
class HospedeListView(generic.ListView):
	model = Hospede

@login_required	
def hospedesprint(request):
	"""Função view para a página hóspedes por id"""
	hospedes = Hospede.objects.all()
	context = {
		'hospedes': hospedes,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'hospedesprint.html', context=context)
    
@login_required	
def hospedesporid(request, pk):
	"""Função view para a página hóspedes por id"""
	hospede = Hospede.objects.get(id=pk)
	context = {
		'hospede': hospede,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'hospedesporid.html', context=context)
    
@login_required	
def hospedesporidprint(request, pk):
	"""Função view para a página hóspedes por id"""
	hospede = Hospede.objects.get(id=pk)
	context = {
		'hospede': hospede,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'hospedesporidprint.html', context=context)

@method_decorator(login_required, name='dispatch')    
class FamiliarListView(generic.ListView):
	model = Familiar

@login_required	
def familiaresprint(request):
	"""Função view para o print da lista de familiares"""
	familiares = Familiar.objects.all()
	context = {
		'familiares': familiares,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'familiaresprint.html', context=context)

@login_required    
def familiarporid(request, pk):
	"""Função view para a página familiares por id"""
	familiar = Familiar.objects.get(id=pk)
	context = {
		'familiar': familiar,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'familiarporid.html', context=context)
    
@login_required    
def familiarporidprint(request, pk):
	"""Função view para a página familiares por id"""
	familiar = Familiar.objects.get(id=pk)
	context = {
		'familiar': familiar,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'familiarporidprint.html', context=context)
 
@method_decorator(login_required, name='dispatch') 
class EquipeListView(generic.ListView):
	model = Equipe

@login_required	
def equipeprint(request):
	"""Função view para o print da lista de familiares"""
	membros = Equipe.objects.all()
	context = {
		'membros': membros,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'equipeprint.html', context=context)

@login_required    
def equipeporid(request, pk):
	"""Função view para a página equipe por id"""
	equipe = Equipe.objects.get(id=pk)
	context = {
		'equipe': equipe,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'equipeporid.html', context=context)
    
@login_required    
def equipeporidprint(request, pk):
	"""Função view para a página equipe por id"""
	equipe = Equipe.objects.get(id=pk)
	context = {
		'equipe': equipe,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'equipeporidprint.html', context=context)

@method_decorator(login_required, name='dispatch')    
class Anotacao_de_EnfermagemListView(generic.ListView):
	model = Anotacao_de_Enfermagem
    
@login_required	
def anotacoesprint(request):
	"""Função view para o print da lista de anotações"""
	anotacoes = Anotacao_de_Enfermagem.objects.all()
	context = {
		'anotacoes': anotacoes,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'anotacoesprint.html', context=context)

@method_decorator(login_required, name='dispatch')    
class Sinais_VitaisListView(generic.ListView):
	model = Sinais_Vitais
    
@login_required	
def sinaisvitaisprint(request):
	"""Função view para o print da lista de sinais vitais"""
	sinaisvitais = Sinais_Vitais.objects.all()
	context = {
		'sinaisvitais': sinaisvitais,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'sinaisvitaisprint.html', context=context)
 
@method_decorator(login_required, name='dispatch') 
class Controle_de_DextroListView(generic.ListView):
	model = Controle_de_Dextro

@login_required	
def dextrosprint(request):
	"""Função view para o print da lista de dextro"""
	dextros = Controle_de_Dextro.objects.all()
	context = {
		'dextros': dextros,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'dextrosprint.html', context=context)

@method_decorator(login_required, name='dispatch')    
class EvolucaoListView(generic.ListView):
	model = Evolucao

@login_required	
def evolucoesprint(request):
	"""Função view para o print da lista de evoluções"""
	evolucoes = Evolucao.objects.all()
	context = {
		'evolucoes': evolucoes,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'evolucoesprint.html', context=context)

@method_decorator(login_required, name='dispatch')    
class MedicacaoListView(generic.ListView):
	model = Medicacao
    
@login_required	
def medicacoesprint(request):
	"""Função view para o print da lista de medicações"""
	medicacoes = Medicacao.objects.all()
	context = {
		'medicacoes': medicacoes,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'medicacoesprint.html', context=context)    

@method_decorator(login_required, name='dispatch')    
class PrescricaoListView(generic.ListView):
	model = Prescricao

@login_required	
def prescricoesprint(request):
	"""Função view para o print da lista de medicações"""
	prescricoes = Prescricao.objects.all()
	context = {
		'prescricoes': prescricoes,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'prescricoesprint.html', context=context)

@method_decorator(login_required, name='dispatch')    
class Ficha_de_AvaliacaoListView(generic.ListView):
	model = Ficha_de_Avaliacao

@login_required
def avaliacoesporid(request, pk):
	"""Função view para a página avaliacões por id"""
	ficha_de_avaliacao = Ficha_de_Avaliacao.objects.get(id=pk)
	context = {
		'ficha_de_avaliacao': ficha_de_avaliacao,
	}
	#Renderiza o template avaliacoesporid.html com os dados na variável context
	return render(request, 'avaliacoesporid.html', context=context)
    
@login_required
def avaliacoesporidprint(request, pk):
	"""Função view para a página avaliacões por id"""
	ficha_de_avaliacao = Ficha_de_Avaliacao.objects.get(id=pk)
	context = {
		'ficha_de_avaliacao': ficha_de_avaliacao,
	}
	#Renderiza o template avaliacoesporid.html com os dados na variável context
	return render(request, 'avaliacoesporidprint.html', context=context)

@method_decorator(login_required, name='dispatch')
class ItemListView(generic.ListView):
	model = Item

@login_required	
def itensprint(request):
	"""Função view para o print da lista de ítens"""
	itens = Item.objects.all()
	context = {
		'itens': itens,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'itensprint.html', context=context)

@method_decorator(login_required, name='dispatch')    
class EstoqueListView(generic.ListView):
	model = Estoque

@login_required	
def estoquesprint(request):
	"""Função view para o print da lista de ítens"""
	estoques = Estoque.objects.all()
	context = {
		'estoques': estoques,
	}
	#Renderiza o template hospedesporid.html com os dados na variável context
	return render(request, 'estoquesprint.html', context=context)

@method_decorator(login_required, name='dispatch')	
class HospedeCreate(CreateView): 
    model = Hospede 
    fields = ['nome_do_hospede', 'sexo', 'data_de_admissao', 'n_de_matricula', 'quarto', 'data_desligamento_obito', 'nascimento', 'n_bdc', 'n_nis',
		'n_cns_sus', 'motivo_da_hospedagem', 'procedencia', 'naturalidade_municipio', 'naturalidade_estado', 'cor_raca', 'pessoa_com_deficiencia',
		'cpf', 'rg', 'rg_emissao', 'rg_orgao_emissor', 'rg_uf', 'certidao_de_nascimento_folha', 'certidao_de_nascimento_livro', 'mae', 'pai',
		'nome_do_responsavel', 'grau_de_parentesco', 'estado_civil', 'grau_de_instrucao', 'profissao', 'ocupacao', 'estado_profissional',
		'endereco_rua', 'endereco_numero', 'endereco_complemento', 'endereco_cep', 'endereco_bairro', 'endereco_distrito', 'telefone_residencial',
		'telefone_celular', 'telefone_outro', 'ponto_de_referencia', 'condicoes_de_moradia', 'n_de_comodos', 'valor_aluguel_ou_financiamento',
		'tipo_de_construcao', 'situacao_habitacional', 'recebe_programa_de_transferencia_de_renda', 'recebe_13_salario', 'parcela1_13',
		'parcela2_13', 'recebe_beneficio_de_prestacao_continuada', 'possui_convenio_medico', 'qual_convenio', 'idoso_recebe_auxilio_para_custo_de_despesas',
		'qual_auxilio', 'demanda_apresentada_orientacoes_encaminhamentos', 'assistente_social', 'data_de_preenchimento_da_ficha', 'observacao'] 
	
@method_decorator(login_required, name='dispatch')
class FamiliarCreate(CreateView): 
    model = Familiar 
    fields = ['hospede','nome','data_de_nascimento','parentesco_vinculo', 'profissao', 'ocupacao', 'renda', 'fatores_de_risco_social', 'estuda',
		'grau_de_instrucao', 'inserido_em_ilpi', 'inserido_em_cedesp', 'inserido_em_nci', 'observacao']

@method_decorator(login_required, name='dispatch')		
class EquipeCreate(CreateView): 
    model = Equipe
    fields = ['nome', 'data_de_nascimento', 'profissao', 'jornada', 'endereco_rua', 'endereco_numero', 'endereco_complemento',
        'endereco_cep', 'endereco_bairro', 'endereco_distrito', 'telefone_residencial', 'telefone_celular', 'telefone_outro', 'observacao']

@method_decorator(login_required, name='dispatch')		
class Anotacao_de_EnfermagemCreate(CreateView): 
    model = Anotacao_de_Enfermagem
    fields = ['hospede','data_hora','anotacao', 'responsavel']

@method_decorator(login_required, name='dispatch')	
class Sinais_VitaisCreate(CreateView): 
    model = Sinais_Vitais
    fields = ['hospede','data_hora', 'pa', 'pulso', 'resp', 'temp', 'sat', 'diures', 'evacuacao', 'observacao', 'responsavel']

@method_decorator(login_required, name='dispatch')	
class Controle_de_DextroCreate(CreateView): 
    model = Controle_de_Dextro
    fields = ['hospede','data_hora', 'dextro', 'observacao', 'responsavel']

@method_decorator(login_required, name='dispatch')	
class EvolucaoCreate(CreateView): 
    model = Evolucao
    fields = ['hospede','data_hora', 'tipo_de_evolucao', 'evolucao', 'responsavel']

@method_decorator(login_required, name='dispatch')	
class MedicacaoCreate(CreateView): 
    model = Medicacao
    fields = ['nome','quantidade', 'unidade', 'fabricante', 'generico']

@method_decorator(login_required, name='dispatch')	
class PrescricaoCreate(CreateView): 
    model = Prescricao
    fields = ['hospede','medicacao', 'dose', 'horario', 'repeticao', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo',
         'data_de_inicio', 'duracao', 'dias_de_duracao', 'data_final', 'data_da_prescricao', 'medico_responsavel', 'observacao']

@method_decorator(login_required, name='dispatch')		 
class Ficha_de_AvaliacaoCreate(CreateView): 
    model = Ficha_de_Avaliacao
    fields = ['hospede', 'enfermidade', 'alergia_medicamentosa', 'qual_alergia_med', 'internacoes_hospitalares', 'data_da_ultima_internacao',
		'duracao_da_internacao', 'motivacao_da_internacao', 'ja_sofreu_quedas', 'ja_teve_fraturas', 'fratura_ha_quanto_tempo',
		'fratura_regiao_acometida', 'ja_foi_submetido_a_cirurgias', 'qual_cirurgia', 'sindrome_respiratoria_aguda', 'SRA_quando', 
		'SRA_se_curou_totalmente', 'SRA_complicacoes', 'vacinado_contra_covid', 'apetite', 'vias_de_alimentacao', 'alteracoes_orais',
		'tipo_de_alimentacao', 'uso_de_tecnicas_assistivas_canudinho_espessante', 'peso_habitual', 'peso_atual', 'perda_de_peso_nos_ultimos_3meses',
		'quanto_perdeu', 'altura', 'imc', 'circunferencia_cintura', 'alergia_alimentar', 'qual_alergia_alimentar', 'preferencia_alimentar',
		'restricao_alimentar', 'eliminacao_intestinal', 'via_de_eliminacao_intestinal', 'eliminacao_urinaria', 'via_de_eliminacao_urinaria',
		'incontinencia_urinaria', 'ciclo_menstrual', 'sono_e_repouso', 'dorme_quantas_horas_por_noite', 'apresenta_dor', 'onde_apresenta_dor',
		'dor_de_cabeca', 'sua_dor_irradia', 'para_onde_irradia', 'quando_a_dor_se_inicia', 'dor_passa_com_medicamento', 'permanece_muito_tempo_sentado',
		'permanece_muito_com_a_cabeca_abaixada', 'possui_lesao_na_coluna_cervical', 'mobilidade_reduzida', 'pressao_arterial', 'saturacao',
		'temperatura', 'pulso', 'FR', 'oxigenacao', 'estado_geral', 'nivel_de_consciencia', 'palidez', 'hidratacao', 'ictericia', 'cianose',
		'tabagismo', 'alcoolismo', 'outras_drogas', 'observacao']

@method_decorator(login_required, name='dispatch')		
class ItemCreate(CreateView): 
    model = Item
    fields = ['nome',]
	
@method_decorator(login_required, name='dispatch')	
class EstoqueCreate(CreateView): 
    model = Estoque
    fields = ['hospede', 'item', 'quantidade']


@method_decorator(login_required, name='dispatch')	
class HospedeUpdate(UpdateView): 
    model = Hospede 
    fields = ['nome_do_hospede', 'sexo', 'data_de_admissao', 'n_de_matricula', 'quarto', 'data_desligamento_obito', 'nascimento', 'n_bdc', 'n_nis',
		'n_cns_sus', 'motivo_da_hospedagem', 'procedencia', 'naturalidade_municipio', 'naturalidade_estado', 'cor_raca', 'pessoa_com_deficiencia',
		'cpf', 'rg', 'rg_emissao', 'rg_orgao_emissor', 'rg_uf', 'certidao_de_nascimento_folha', 'certidao_de_nascimento_livro', 'mae', 'pai',
		'nome_do_responsavel', 'grau_de_parentesco', 'estado_civil', 'grau_de_instrucao', 'profissao', 'ocupacao', 'estado_profissional',
		'endereco_rua', 'endereco_numero', 'endereco_complemento', 'endereco_cep', 'endereco_bairro', 'endereco_distrito', 'telefone_residencial',
		'telefone_celular', 'telefone_outro', 'ponto_de_referencia', 'condicoes_de_moradia', 'n_de_comodos', 'valor_aluguel_ou_financiamento',
		'tipo_de_construcao', 'situacao_habitacional', 'recebe_programa_de_transferencia_de_renda', 'recebe_13_salario', 'parcela1_13',
		'parcela2_13', 'recebe_beneficio_de_prestacao_continuada', 'possui_convenio_medico', 'qual_convenio', 'idoso_recebe_auxilio_para_custo_de_despesas',
		'qual_auxilio', 'demanda_apresentada_orientacoes_encaminhamentos', 'assistente_social', 'data_de_preenchimento_da_ficha', 'observacao']
        
@method_decorator(login_required, name='dispatch')	
class HospedeDelete(DeleteView): 
    model = Hospede 
    success_url = reverse_lazy('hospedes')

@method_decorator(login_required, name='dispatch')	
class FamiliarUpdate(UpdateView): 
    model = Familiar
    fields = ['hospede','nome','data_de_nascimento','parentesco_vinculo', 'profissao', 'ocupacao', 'renda', 'fatores_de_risco_social', 'estuda',
		'grau_de_instrucao', 'inserido_em_ilpi', 'inserido_em_cedesp', 'inserido_em_nci', 'observacao']
        
@method_decorator(login_required, name='dispatch')	
class FamiliarDelete(DeleteView): 
    model = Familiar 
    success_url = reverse_lazy('familiares')

@method_decorator(login_required, name='dispatch')	
class EquipeUpdate(UpdateView): 
    model = Equipe
    fields = ['nome', 'data_de_nascimento', 'profissao', 'jornada', 'endereco_rua', 'endereco_numero', 'endereco_complemento',
        'endereco_cep', 'endereco_bairro', 'endereco_distrito', 'telefone_residencial', 'telefone_celular', 'telefone_outro', 'observacao']
        
@method_decorator(login_required, name='dispatch')	
class EquipeDelete(DeleteView): 
    model = Equipe 
    success_url = reverse_lazy('equipe')    
    
@method_decorator(login_required, name='dispatch')	
class Anotacao_de_EnfermagemUpdate(UpdateView): 
    model = Anotacao_de_Enfermagem
    fields = ['hospede','data_hora','anotacao', 'responsavel']
        
@method_decorator(login_required, name='dispatch')	
class Anotacao_de_EnfermagemDelete(DeleteView): 
    model = Anotacao_de_Enfermagem 
    success_url = reverse_lazy('anotacoes')
    
@method_decorator(login_required, name='dispatch')	
class Sinais_VitaisUpdate(UpdateView): 
    model = Sinais_Vitais
    fields = ['hospede','data_hora', 'pa', 'pulso', 'resp', 'temp', 'sat', 'diures', 'evacuacao', 'observacao', 'responsavel']
        
@method_decorator(login_required, name='dispatch')	
class Sinais_VitaisDelete(DeleteView): 
    model = Sinais_Vitais
    success_url = reverse_lazy('sinaisvitais')
    
@method_decorator(login_required, name='dispatch')	
class Controle_de_DextroUpdate(UpdateView): 
    model = Controle_de_Dextro
    fields = ['hospede','data_hora', 'dextro', 'responsavel']
        
@method_decorator(login_required, name='dispatch')	
class Controle_de_DextroDelete(DeleteView): 
    model = Controle_de_Dextro
    success_url = reverse_lazy('dextro')
    
@method_decorator(login_required, name='dispatch')	
class EvolucaoUpdate(UpdateView): 
    model = Evolucao
    fields = ['hospede','data_hora', 'tipo_de_evolucao', 'evolucao', 'responsavel']
        
@method_decorator(login_required, name='dispatch')	
class EvolucaoDelete(DeleteView): 
    model = Evolucao
    success_url = reverse_lazy('evolucoes')
    
@method_decorator(login_required, name='dispatch')	
class MedicacaoUpdate(UpdateView): 
    model = Medicacao
    fields = ['nome','quantidade', 'unidade', 'fabricante', 'generico']
        
@method_decorator(login_required, name='dispatch')	
class MedicacaoDelete(DeleteView): 
    model = Medicacao
    success_url = reverse_lazy('medicacoes')
    
@method_decorator(login_required, name='dispatch')	
class PrescricaoUpdate(UpdateView): 
    model = Prescricao
    fields = ['hospede','medicacao', 'dose', 'horario', 'repeticao', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo',
         'data_de_inicio', 'duracao', 'dias_de_duracao', 'data_final', 'data_da_prescricao', 'medico_responsavel', 'observacao']
        
@method_decorator(login_required, name='dispatch')	
class PrescricaoDelete(DeleteView): 
    model = Prescricao
    success_url = reverse_lazy('prescricoes')
    
@method_decorator(login_required, name='dispatch')	
class Ficha_de_AvaliacaoUpdate(UpdateView): 
    model = Ficha_de_Avaliacao
    fields = ['hospede', 'enfermidade', 'alergia_medicamentosa', 'qual_alergia_med', 'internacoes_hospitalares', 'data_da_ultima_internacao',
		'duracao_da_internacao', 'motivacao_da_internacao', 'ja_sofreu_quedas', 'ja_teve_fraturas', 'fratura_ha_quanto_tempo',
		'fratura_regiao_acometida', 'ja_foi_submetido_a_cirurgias', 'qual_cirurgia', 'sindrome_respiratoria_aguda', 'SRA_quando', 
		'SRA_se_curou_totalmente', 'SRA_complicacoes', 'vacinado_contra_covid', 'apetite', 'vias_de_alimentacao', 'alteracoes_orais',
		'tipo_de_alimentacao', 'uso_de_tecnicas_assistivas_canudinho_espessante', 'peso_habitual', 'peso_atual', 'perda_de_peso_nos_ultimos_3meses',
		'quanto_perdeu', 'altura', 'imc', 'circunferencia_cintura', 'alergia_alimentar', 'qual_alergia_alimentar', 'preferencia_alimentar',
		'restricao_alimentar', 'eliminacao_intestinal', 'via_de_eliminacao_intestinal', 'eliminacao_urinaria', 'via_de_eliminacao_urinaria',
		'incontinencia_urinaria', 'ciclo_menstrual', 'sono_e_repouso', 'dorme_quantas_horas_por_noite', 'apresenta_dor', 'onde_apresenta_dor',
		'dor_de_cabeca', 'sua_dor_irradia', 'para_onde_irradia', 'quando_a_dor_se_inicia', 'dor_passa_com_medicamento', 'permanece_muito_tempo_sentado',
		'permanece_muito_com_a_cabeca_abaixada', 'possui_lesao_na_coluna_cervical', 'mobilidade_reduzida', 'pressao_arterial', 'saturacao',
		'temperatura', 'pulso', 'FR', 'oxigenacao', 'estado_geral', 'nivel_de_consciencia', 'palidez', 'hidratacao', 'ictericia', 'cianose',
		'tabagismo', 'alcoolismo', 'outras_drogas', 'observacao']
        
@method_decorator(login_required, name='dispatch')	
class Ficha_de_AvaliacaoDelete(DeleteView): 
    model = Ficha_de_Avaliacao
    success_url = reverse_lazy('avaliacoes')
    
@method_decorator(login_required, name='dispatch')	
class ItemUpdate(UpdateView): 
    model = Item
    fields = ['nome',]
        
@method_decorator(login_required, name='dispatch')	
class ItemDelete(DeleteView): 
    model = Item
    success_url = reverse_lazy('itens')
    
@method_decorator(login_required, name='dispatch')	
class EstoqueUpdate(UpdateView): 
    model = Estoque
    fields = ['hospede', 'item', 'quantidade']
        
@method_decorator(login_required, name='dispatch')	
class EstoqueDelete(DeleteView): 
    model = Estoque
    success_url = reverse_lazy('estoque')