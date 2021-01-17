# Generated by Django 3.1.5 on 2021-01-17 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0010_auto_20210117_1237'),
    ]

    operations = [
        migrations.CreateModel(
            name='TemporaryContraindications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(null=True)),
                ('text_to_onclusion', models.TextField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='coagupathy',
        ),
        migrations.RemoveField(
            model_name='treatment',
            name='takes_anticoagulants',
        ),
        migrations.AddField(
            model_name='diagnosis',
            name='text_to_onclusion',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='treatment',
            name='temporary_contraindications',
            field=models.ManyToManyField(null=True, to='web.TemporaryContraindications'),
        ),
    ]
