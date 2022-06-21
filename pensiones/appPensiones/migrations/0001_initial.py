# Generated by Django 3.2.13 on 2022-05-02 23:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('edadActual', models.IntegerField(default=0)),
                ('edadRetiro', models.IntegerField(default=0)),
                ('saldoAcumulado', models.FloatField(default=0.0)),
                ('ahorroMensual', models.FloatField(default=0.0)),
                ('genero', models.IntegerField(default=0)),
            ],
        ),
    ]