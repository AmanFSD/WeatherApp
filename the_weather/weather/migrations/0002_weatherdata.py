# Generated by Django 3.2.8 on 2021-10-24 09:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WeatherData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('temp', models.FloatField()),
                ('description', models.CharField(max_length=100)),
                ('icon', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
        ),
    ]