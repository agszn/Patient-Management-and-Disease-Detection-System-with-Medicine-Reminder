# Generated by Django 5.0.3 on 2024-04-27 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("smartmedical", "0002_remove_patient_groups_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prescription",
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
                ("user_name", models.CharField(max_length=100)),
                ("user_id", models.IntegerField()),
                ("registered_username", models.CharField(max_length=100)),
                ("appointment_title", models.CharField(max_length=200)),
                ("appointment_description", models.TextField()),
                ("appointment_date", models.DateField()),
                ("appointment_time", models.TimeField()),
                (
                    "report_document",
                    models.FileField(upload_to="prescription_reports/"),
                ),
                ("medicine_name", models.CharField(max_length=200)),
                ("time_to_be_taken", models.TimeField()),
                ("number_of_days", models.IntegerField()),
                (
                    "before_or_after_meals",
                    models.CharField(
                        choices=[("before", "Before meals"), ("after", "After meals")],
                        max_length=10,
                    ),
                ),
                ("exercise_name", models.CharField(max_length=200)),
                (
                    "exercise_type",
                    models.CharField(
                        choices=[
                            ("aerobic", "Aerobic"),
                            ("strength", "Strength"),
                            ("flexibility", "Flexibility"),
                        ],
                        max_length=20,
                    ),
                ),
                ("exercise_time", models.TimeField()),
                ("experience", models.TextField()),
            ],
        ),
    ]
