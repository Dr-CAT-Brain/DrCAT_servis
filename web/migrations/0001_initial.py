# Generated by Django 3.1.5 on 2021-01-20 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('text_to_onclusion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(default='Фамилия Имя Отчество', max_length=100)),
                ('qualification', models.CharField(blank=True, max_length=100, null=True)),
                ('experience', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('work_place', models.CharField(blank=True, max_length=100, null=True)),
                ('education', models.CharField(blank=True, max_length=100, null=True)),
                ('contacts', models.CharField(blank=True, max_length=100, null=True)),
                ('photo', models.ImageField(default='BaseProfilePhoto.svd', null=True, upload_to='')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(blank=True, max_length=100, null=True)),
                ('age', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('diagnoses', models.ManyToManyField(to='web.Diagnosis')),
            ],
        ),
        migrations.CreateModel(
            name='TemporaryContraindications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('text_to_onclusion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Treatment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('neurological_deficit', models.PositiveSmallIntegerField(default=1)),
                ('conscious_level', models.PositiveSmallIntegerField(default=15)),
                ('time_passed', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('hematoma_volume', models.PositiveSmallIntegerField(blank=True, null=True)),
                ('is_injury', models.BooleanField(blank=True, default=False, null=True)),
                ('has_stroke_symptoms', models.BooleanField(default=False)),
                ('snapshot', models.ImageField(blank=True, null=True, upload_to='snapshots')),
                ('doctor', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.doctor')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.patient')),
                ('temporary_contraindications', models.ManyToManyField(to='web.TemporaryContraindications')),
            ],
        ),
        migrations.CreateModel(
            name='NeuronetPrediction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('classification_type', models.PositiveSmallIntegerField()),
                ('confidence', models.PositiveSmallIntegerField(null=True)),
                ('treatment', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='web.treatment')),
            ],
        ),
    ]
