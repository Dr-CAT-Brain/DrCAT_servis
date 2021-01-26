# Generated by Django 3.1.5 on 2021-01-24 12:21

from django.db import migrations, models
import django.db.models.deletion
import web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20210120_1840'),
    ]

    operations = [
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='doctor',
            name='full_name',
            field=models.CharField(default='Фамилия имя отчество', max_length=100),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='photo',
            field=models.ImageField(default='profile_photo.jpg', null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='neuronetprediction',
            name='recommend_text',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='web.recommendtext', null=True),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='snapshot',
            field=models.ImageField(blank=True, null=True, upload_to=web.models.rename_file_by_pk),
        ),
        migrations.CreateModel(
            name='FAQItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('reference', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='web.faq')),
            ],
        ),
    ]