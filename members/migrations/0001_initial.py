# Generated by Django 3.1.5 on 2021-01-15 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(verbose_name='URL')),
                ('name', models.CharField(max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=100, verbose_name='E-mail')),
                ('birth', models.DateField(verbose_name='Data de Nascimento')),
                ('gender', models.CharField(choices=[(None, 'Escolha seu Gênero'), ('Masculino', 'Masculino'), ('Feminino', 'Feminino')], max_length=10, verbose_name='Gênero')),
                ('blood', models.CharField(choices=[(None, 'Escolha seu Tipo Sanguíneo'), ('Tipo A+', 'Tipo A+'), ('Tipo A-', 'Tipo A-'), ('Tipo B+', 'Tipo B+'), ('Tipo B-', 'Tipo B-'), ('Tipo O+', 'Tipo O+'), ('Tipo O-', 'Tipo O-'), ('Tipo AB+', 'Tipo AB+'), ('Tipo AB-', 'Tipo AB-')], max_length=10, verbose_name='Tipo Sanguíneo')),
                ('weight', models.FloatField(verbose_name='Peso')),
                ('height', models.FloatField(verbose_name='Altura')),
            ],
            options={
                'verbose_name': 'Membro',
                'verbose_name_plural': 'Membros',
            },
        ),
    ]
