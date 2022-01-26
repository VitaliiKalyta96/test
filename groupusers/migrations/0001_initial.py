# Generated by Django 3.2.9 on 2022-01-24 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='User name')),
                ('description', models.CharField(max_length=255, verbose_name='Description')),
            ],
        ),
    ]
