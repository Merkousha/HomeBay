# Generated by Django 3.2.20 on 2023-10-28 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RealState', '0007_alter_property_images_property'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property_images',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
