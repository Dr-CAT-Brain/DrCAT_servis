# Generated by Django 3.1.5 on 2021-01-12 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20210112_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='snapshot',
            field=models.ImageField(null=True, upload_to='media/snapshots'),
        ),
    ]
