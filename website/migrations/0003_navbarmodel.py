# Generated by Django 4.1.5 on 2023-01-25 19:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0002_homepagemodel_second_part"),
    ]

    operations = [
        migrations.CreateModel(
            name="NavBarModel",
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
                ("title", models.CharField(max_length=50)),
            ],
        ),
    ]
