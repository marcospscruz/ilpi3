# Generated by Django 4.1.1 on 2022-10-16 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('betel', '0031_alter_familiar_fatores_de_risco_social_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='estoque',
            options={'ordering': ['hospede', 'item']},
        ),
    ]