# Generated by Django 4.1.1 on 2022-11-04 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betel', '0034_alter_evolucao_tipo_de_evolucao_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='hospede',
            name='quarto',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='hospede',
            name='n_cns_sus',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='hospede',
            name='nascimento',
            field=models.DateField(help_text='Formato: AAAA-MM-DD'),
        ),
        migrations.AlterField(
            model_name='hospede',
            name='nome_do_hospede',
            field=models.CharField(help_text='Insira o nome do hóspede', max_length=50),
        ),
        migrations.AlterField(
            model_name='hospede',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=1),
        ),
    ]
