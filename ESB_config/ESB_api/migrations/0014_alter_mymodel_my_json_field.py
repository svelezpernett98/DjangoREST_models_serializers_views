# Generated by Django 4.0.5 on 2022-06-17 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ESB_api', '0013_mymodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymodel',
            name='my_json_field',
            field=models.JSONField(default=dict),
        ),
    ]