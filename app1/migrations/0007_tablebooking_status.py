# Generated by Django 2.1.5 on 2021-12-27 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20211227_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablebooking',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
