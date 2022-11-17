from betel.models import Hospede, Fator_de_Risco_Social, Familiar, Equipe, Anotacao_de_Enfermagem, Sinais_Vitais, Controle_de_Dextro, Evolucao, Medicacao, Prescricao, Enfermidade, Ficha_de_Avaliacao, Item, Estoque   
from rest_framework import serializers 


class HospedeSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Hospede 
        fields = ['id','nome_do_hospede','sexo', 'data_de_admissao', 'n_de_matricula', 'quarto', 'data_desligamento_obito', 'nascimento', 'n_bdc', 'n_nis',
		'n_cns_sus', 'motivo_da_hospedagem', 'procedencia', 'naturalidade_municipio', 'naturalidade_estado', 'cor_raca', 'pessoa_com_deficiencia',
		'cpf', 'rg', 'rg_emissao', 'rg_orgao_emissor', 'rg_uf', 'certidao_de_nascimento_folha', 'certidao_de_nascimento_livro', 'mae', 'pai',
		'nome_do_responsavel', 'grau_de_parentesco', 'estado_civil', 'grau_de_instrucao', 'profissao', 'ocupacao', 'estado_profissional',
		'endereco_rua', 'endereco_numero', 'endereco_complemento', 'endereco_cep', 'endereco_bairro', 'endereco_distrito', 'telefone_residencial',
		'telefone_celular', 'telefone_outro', 'ponto_de_referencia', 'condicoes_de_moradia', 'n_de_comodos', 'valor_aluguel_ou_financiamento',
		'tipo_de_construcao', 'situacao_habitacional', 'recebe_programa_de_transferencia_de_renda', 'recebe_13_salario', 'parcela1_13', 'parcela2_13',
		'recebe_beneficio_de_prestacao_continuada', 'possui_convenio_medico', 'qual_convenio', 'idoso_recebe_auxilio_para_custo_de_despesas',
		'qual_auxilio', 'demanda_apresentada_orientacoes_encaminhamentos', 'assistente_social', 'data_de_preenchimento_da_ficha', 'observacao']


class Fator_de_Risco_SocialSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Fator_de_Risco_Social 
        fields = ['id','nome',] 
		

class FamiliarSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Familiar 
        fields = ['id','hospede','nome', 'data_de_nascimento', 'parentesco_vinculo', 'profissao', 'ocupacao', 'renda', 'fatores_de_risco_social',
		'estuda', 'grau_de_instrucao', 'inserido_em_ilpi', 'inserido_em_cedesp', 'inserido_em_nci', 'observacao'] 

class EquipeSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Equipe 
        fields = ['id','nome', 'data_de_nascimento', 'profissao', 'jornada', 'endereco_rua', 'endereco_numero', 'endereco_complemento',
		'endereco_cep', 'endereco_bairro', 'endereco_distrito', 'telefone_residencial', 'telefone_celular', 'telefone_outro', 'observacao'] 		
		
class Anotacao_de_EnfermagemSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Anotacao_de_Enfermagem 
        fields = ['id','hospede','data_hora', 'anotacao', 'responsavel',] 
		
		
class Sinais_VitaisSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Sinais_Vitais 
        fields = ['id','hospede','data_hora', 'pa', 'pulso', 'resp', 'temp', 'sat', 'diures', 'evacuacao', 'observacao', 'responsavel'] 
		

class Controle_de_DextroSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Controle_de_Dextro
        fields = ['id','hospede','data_hora', 'dextro', 'observacao', 'responsavel',] 

class EvolucaoSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Evolucao
        fields = ['id','hospede','data_hora', 'tipo_de_evolucao', 'evolucao', 'responsavel',] 

class MedicacaoSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Medicacao
        fields = ['id','nome','quantidade', 'unidade', 'fabricante', 'generico',]

class PrescricaoSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Prescricao
        fields = ['id','hospede','medicacao', 'dose', 'horario', 'repeticao', 'segunda', 'terca', 'quarta', 'quinta', 'sexta', 'sabado', 'domingo',
		'data_de_inicio', 'duracao', 'dias_de_duracao', 'data_final', 'data_da_prescricao', 'medico_responsavel', 'observacao']

class EnfermidadeSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Enfermidade
        fields = ['id','nome',] 

class Ficha_de_AvaliacaoSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Ficha_de_Avaliacao
        fields = ['id','hospede', 'enfermidade', 'alergia_medicamentosa', 'qual_alergia_med', 'internacoes_hospitalares', 'data_da_ultima_internacao',
		'duracao_da_internacao', 'motivacao_da_internacao', 'ja_sofreu_quedas', 'ja_teve_fraturas', 'fratura_ha_quanto_tempo', 'fratura_regiao_acometida',
		'ja_foi_submetido_a_cirurgias', 'qual_cirurgia', 'sindrome_respiratoria_aguda', 'SRA_quando', 'SRA_se_curou_totalmente', 'SRA_complicacoes',
		'vacinado_contra_covid', 'apetite', 'vias_de_alimentacao', 'alteracoes_orais', 'tipo_de_alimentacao', 'uso_de_tecnicas_assistivas_canudinho_espessante',
		'peso_habitual', 'peso_atual', 'perda_de_peso_nos_ultimos_3meses', 'quanto_perdeu', 'altura', 'imc', 'circunferencia_cintura', 'alergia_alimentar',
		'qual_alergia_alimentar', 'preferencia_alimentar', 'restricao_alimentar', 'eliminacao_intestinal', 'via_de_eliminacao_intestinal', 'eliminacao_urinaria',
		'via_de_eliminacao_urinaria', 'incontinencia_urinaria', 'ciclo_menstrual', 'sono_e_repouso', 'dorme_quantas_horas_por_noite', 'apresenta_dor',
		'onde_apresenta_dor', 'dor_de_cabeca', 'sua_dor_irradia', 'para_onde_irradia', 'quando_a_dor_se_inicia', 'dor_passa_com_medicamento',
		'permanece_muito_tempo_sentado', 'permanece_muito_com_a_cabeca_abaixada', 'possui_lesao_na_coluna_cervical', 'mobilidade_reduzida',
		'pressao_arterial', 'saturacao', 'temperatura', 'pulso', 'FR', 'oxigenacao', 'estado_geral', 'nivel_de_consciencia', 'palidez', 'hidratacao',
		'ictericia', 'cianose', 'tabagismo', 'alcoolismo', 'outras_drogas', 'observacao']

class ItemSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Item
        fields = ['id','nome',]  

class EstoqueSerializer(serializers.HyperlinkedModelSerializer): 

    class Meta: 
        model = Estoque
        fields = ['id','hospede', 'item', 'quantidade']		