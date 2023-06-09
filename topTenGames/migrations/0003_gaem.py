# Generated by Django 4.2.1 on 2023-05-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('topTenGames', '0002_alter_game_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gaem',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('platform', models.CharField(blank=True, max_length=10)),
                ('year', models.IntegerField(blank=True)),
                ('genre', models.CharField(blank=True, max_length=128)),
                ('publisher', models.CharField(blank=True, max_length=128)),
                ('euSales', models.FloatField()),
                ('jpSales', models.FloatField()),
                ('otherSales', models.FloatField()),
                ('naSales', models.FloatField()),
                ('globalSales', models.FloatField()),
            ],
        ),
    ]
