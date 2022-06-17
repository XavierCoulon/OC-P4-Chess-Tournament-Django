# Generated by Django 4.0.5 on 2022-06-17 13:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=128, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=128, unique=True)),
                ('last_name', models.CharField(max_length=128, unique=True)),
                ('ranking', models.IntegerField(unique=True)),
                ('birth_date', models.DateField()),
                ('description', models.CharField(max_length=128, unique=True)),
                ('gender', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='player.gender')),
            ],
        ),
    ]
