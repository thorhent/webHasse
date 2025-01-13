# Generated by Django 5.1.4 on 2025-01-13 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clima',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tempo', models.CharField(choices=[('Sol', 'Sol'), ('Nublado', 'Nublado'), ('Chuva', 'Chuva')], max_length=50, verbose_name='Tempo do dia')),
                ('qtd', models.IntegerField(default=0, help_text='Quantidade de milímetros (mm) de chuva. Exemplo: 25', verbose_name='quantidade de chuva (mm)')),
                ('data', models.DateField(unique=True, verbose_name='data de chuva')),
            ],
            options={
                'verbose_name': 'Clima',
                'verbose_name_plural': 'Climas',
            },
        ),
    ]