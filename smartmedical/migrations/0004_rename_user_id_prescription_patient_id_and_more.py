# Generated by Django 5.0.3 on 2024-04-27 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("smartmedical", "0003_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="prescription",
            old_name="user_id",
            new_name="patient_id",
        ),
        migrations.RenameField(
            model_name="prescription",
            old_name="user_name",
            new_name="patient_name",
        ),
    ]
