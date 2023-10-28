# Generated by Django 4.2.6 on 2023-10-28 11:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("RealState", "0002_property_property_images"),
    ]

    operations = [
        migrations.CreateModel(
            name="Builder",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.TextField(max_length=20)),
                ("description", models.TextField(max_length=2000)),
                ("picture", models.ImageField(blank=True, null=True, upload_to="")),
            ],
        ),
        migrations.AddField(
            model_name="property",
            name="Builder",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="RealState.builder",
            ),
        ),
    ]
