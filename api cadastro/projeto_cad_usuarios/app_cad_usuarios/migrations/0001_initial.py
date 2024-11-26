# Generated by Django 5.1.3 on 2024-11-26 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.TextField(max_length=255)),
                ('sobrenome', models.TextField(max_length=255)),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('idade', models.IntegerField()),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.TextField(max_length=255)),
                ('endereco_imovel', models.TextField(max_length=255)),
                ('senha', models.CharField(max_length=255)),
            ],
        ),
    ]
