# Generated by Django 3.1.5 on 2021-01-13 08:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_auto_20210113_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='treatment',
            name='patient',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='web.patient'),
            preserve_default=False,
        ),
    ]