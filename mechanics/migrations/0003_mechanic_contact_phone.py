# Generated by Django 5.2 on 2025-05-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("mechanics", "0002_mechanic_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="mechanic",
            name="contact_phone",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
