# Generated by Django 4.0.5 on 2022-06-23 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('round', '0002_alter_round_end_date_alter_round_start_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='round',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='round',
            name='start_date',
            field=models.DateField(),
        ),
    ]