# Generated by Django 4.1.1 on 2022-10-05 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "betel",
            "0027_rename_sra_complicacoes_ficha_de_avaliacao_sra_complicacoes_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="altura",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="apetite",
            field=models.CharField(
                blank=True,
                choices=[("BOM", "Bom"), ("RUI", "Ruim")],
                max_length=3,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="apresenta_dor",
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="ciclo_menstrual",
            field=models.CharField(
                blank=True,
                choices=[
                    ("SA", "Sem alterações"),
                    ("MP", "Menopausa"),
                    ("AD", "Amenorréia Disfuncional"),
                ],
                max_length=2,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="circunferencia_cintura",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="dor_de_cabeca",
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="dor_passa_com_medicamento",
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="dorme_quantas_horas_por_noite",
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="eliminacao_intestinal",
            field=models.CharField(
                blank=True,
                choices=[
                    ("NOR", "Normal"),
                    ("CON", "Constipação"),
                    ("DIA", "Diarreia"),
                    ("MHI", "Mudança de hábito Intestinal"),
                ],
                max_length=3,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="eliminacao_urinaria",
            field=models.CharField(
                blank=True,
                choices=[
                    ("NOR", "Normal"),
                    ("M5V", "Menos de 5 vezes por dia"),
                    ("POL", "Polaciúria"),
                    ("NIC", "Nicturia"),
                    ("URG", "Urgência Miccional"),
                    ("DIM", "Diminuição do jato"),
                ],
                max_length=3,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="imc",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="mobilidade_reduzida",
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="onde_apresenta_dor",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="para_onde_irradia",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="permanece_muito_com_a_cabeca_abaixada",
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="permanece_muito_tempo_sentado",
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="peso_atual",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="peso_habitual",
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="possui_lesao_na_coluna_cervical",
            field=models.BooleanField(null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="quando_a_dor_se_inicia",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="sono_e_repouso",
            field=models.CharField(
                blank=True,
                choices=[
                    ("NTI", "Não tem insonia"),
                    ("DCS", "Apresenta dificuldade em conciliar o sono"),
                    ("AVV", "Acorda várias vezes"),
                    ("SON", "Sonolência"),
                    ("DDD", "Dorme durante o dia"),
                    ("TIO", "Tem insônia em outro local"),
                ],
                max_length=3,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="ficha_de_avaliacao",
            name="sua_dor_irradia",
            field=models.BooleanField(null=True),
        ),
    ]