# Generated by Django 4.1.5 on 2023-01-26 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("website", "0005_remove_statsmodel_about"),
    ]

    operations = [
        migrations.AddField(
            model_name="aboutmodel",
            name="image",
            field=models.ImageField(default=None, upload_to="media/"),
        ),
    ]