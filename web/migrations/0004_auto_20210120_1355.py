# Generated by Django 3.1.5 on 2021-01-20 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20210120_1334'),
    ]

    operations = [
        migrations.AlterField(
            model_name='neuronetprediction',
            name='confidence',
            field=models.FloatField(null=True),
        ),
    ]