# Generated by Django 5.2 on 2025-05-12 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reviews", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="review",
            name="updated_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
