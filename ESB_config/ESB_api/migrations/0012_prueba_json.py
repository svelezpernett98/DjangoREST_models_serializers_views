# Generated by Django 4.0.5 on 2022-06-17 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESB_api', '0011_rename_hora_factura_fecha_hora_remove_factura_fecha'),
    ]

    operations = [
        migrations.CreateModel(
            name='Prueba_json',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('campo_json', models.JSONField(blank=True, default=list, null=True, verbose_name='campo_json')),
            ],
        ),
    ]