# Generated by Django 2.1.5 on 2021-10-20 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_product_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ImageField(blank=True, default='', upload_to='pro_img'),
        ),
    ]