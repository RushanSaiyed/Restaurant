# Generated by Django 2.1.5 on 2021-10-15 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20211012_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=80),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(max_length=80),
        ),
    ]