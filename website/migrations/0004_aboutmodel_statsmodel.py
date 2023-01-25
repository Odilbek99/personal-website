# Generated by Django 4.1.5 on 2023-01-25 20:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0003_navbarmodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="AboutModel",
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
                (
                    "title",
                    models.CharField(default="LEARN MORE ABOUT ME", max_length=255),
                ),
                (
                    "whoami",
                    models.CharField(
                        default="Data Scientist/Python Developer", max_length=255
                    ),
                ),
                ("birthday", models.DateField()),
                ("website", models.URLField()),
                ("phone", models.CharField(max_length=15)),
                ("city", models.CharField(max_length=25)),
                ("age", models.IntegerField()),
                (
                    "degree",
                    models.CharField(
                        choices=[
                            ("BACHELOR", "Bachelor"),
                            ("MASTER", "Master"),
                            ("PHD", "PhD"),
                        ],
                        default="BACHELOR",
                        max_length=25,
                    ),
                ),
                ("email", models.EmailField(max_length=255)),
                (
                    "freelance",
                    models.CharField(
                        choices=[
                            ("AVAILABLE", "Available"),
                            ("NOT_AVAILABLE", "Not Available"),
                        ],
                        default="NOT AVAILABLE",
                        max_length=25,
                    ),
                ),
                ("about_me", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="StatsModel",
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
                (
                    "title",
                    models.CharField(
                        help_text="Projects, Awards etc..", max_length=255
                    ),
                ),
                ("number", models.IntegerField(help_text="Projects, Awards etc..")),
                (
                    "icon",
                    models.CharField(
                        help_text="ccopy icon class from https://icons.getbootstrap.com/",
                        max_length=255,
                    ),
                ),
                (
                    "about",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="stats",
                        to="website.aboutmodel",
                    ),
                ),
            ],
        ),
    ]
