# Generated by Django 4.0.5 on 2022-06-13 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESB_api', '0002_rename_id_clientes_cedula_alter_clientes_correo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientes',
            name='correo',
            field=models.CharField(max_length=30),
        ),
    ]