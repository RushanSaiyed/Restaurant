# Generated by Django 2.1.5 on 2021-12-27 07:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_tablebooking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablebooking',
            name='capacity',
            field=models.IntegerField(default=''),
        ),
    ]
