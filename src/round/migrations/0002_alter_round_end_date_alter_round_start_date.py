# Generated by Django 4.0.5 on 2022-06-23 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('round', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='end_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='round',
            name='start_date',
            field=models.DateField(blank=True),
        ),
    ]