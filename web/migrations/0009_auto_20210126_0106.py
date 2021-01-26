# Generated by Django 3.1.5 on 2021-01-25 20:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_auto_20210124_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='neuronetprediction',
            name='classification_types',
        ),
        migrations.CreateModel(
            name='ClassificationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveSmallIntegerField()),
                ('prediction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classification_types', to='web.neuronetprediction')),
            ],
        ),
    ]