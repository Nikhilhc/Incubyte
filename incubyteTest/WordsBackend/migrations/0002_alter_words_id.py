# Generated by Django 4.0.3 on 2022-03-26 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WordsBackend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='words',
            name='id',
            field=models.IntegerField(blank=True, primary_key=True, serialize=False),
        ),
    ]
