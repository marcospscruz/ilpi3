# Generated by Django 4.1.1 on 2022-10-02 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('betel', '0014_evolucao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evolucao',
            name='evolucao',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
    ]
