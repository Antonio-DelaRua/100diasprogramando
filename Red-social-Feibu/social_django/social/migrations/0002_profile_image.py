# Generated by Django 4.2.2 on 2023-06-21 16:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("social", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="image",
            field=models.ImageField(default="batman.png", upload_to=""),
        ),
    ]
