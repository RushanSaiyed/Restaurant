# Generated by Django 2.1.5 on 2021-12-27 08:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0009_bookingdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.IntegerField(),
        ),
    ]