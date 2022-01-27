# Generated by Django 2.1.5 on 2021-12-27 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20211223_1343'),
    ]

    operations = [
        migrations.CreateModel(
            name='table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.ImageField(blank=True, default='', upload_to='pro_img')),
                ('capacity', models.IntegerField(default='', max_length=20)),
            ],
        ),
    ]