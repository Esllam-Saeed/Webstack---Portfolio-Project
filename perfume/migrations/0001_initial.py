# Generated by Django 5.0.6 on 2024-05-26 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('brand', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('image', models.CharField(max_length=2083)),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
