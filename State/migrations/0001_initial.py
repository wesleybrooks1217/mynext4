# Generated by Django 4.1.3 on 2023-01-13 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="State",
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
                ("meritAID", models.BooleanField()),
                ("gpaAID", models.FloatField(blank=True)),
                ("satAID", models.IntegerField(blank=True)),
                ("actAID", models.IntegerField(blank=True)),
                ("freeCommunityCollege", models.BooleanField()),
                ("deAID", models.BooleanField()),
                (
                    "deAIDyear",
                    models.IntegerField(
                        choices=[(9, "9th"), (10, "10th"), (11, "11th"), (12, "12th")],
                        default=11,
                    ),
                ),
                ("deAIDgpa", models.FloatField(blank=True)),
                ("deAIDsat", models.IntegerField(blank=True)),
                ("deAIDact", models.IntegerField(blank=True)),
                ("techSchoolAID", models.BooleanField()),
                ("onlineCourseProgram", models.BooleanField()),
                ("onlineCourseAID", models.BooleanField()),
            ],
        ),
    ]
