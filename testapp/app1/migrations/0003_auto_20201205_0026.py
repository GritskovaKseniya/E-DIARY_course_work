# Generated by Django 3.1.2 on 2020-12-04 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_loguser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='login',
            field=models.CharField(max_length=200, unique=True, verbose_name='Логин'),
        ),
        migrations.AlterField(
            model_name='teachers',
            name='login',
            field=models.CharField(max_length=200, unique=True, verbose_name='Логин'),
        ),
    ]
