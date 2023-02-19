# Generated by Django 4.1.3 on 2023-02-17 18:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("courses", "0001_initial"),
        ("duelEnrollmentCourses", "0001_initial"),
        ("State", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="School",
            fields=[
                (
                    "id",
                    models.IntegerField(
                        max_length=1000000000, primary_key=True, serialize=False
                    ),
                ),
                ("name", models.CharField(max_length=175)),
                ("DEallowed", models.BooleanField()),
                ("schoolAddress", models.CharField(max_length=350)),
                ("englishUnits", models.IntegerField()),
                ("mathUnits", models.IntegerField()),
                ("scienceUnits", models.IntegerField()),
                ("socialStudiesUnits", models.IntegerField()),
                ("humanityUnits", models.IntegerField()),
                ("CTAEunits", models.IntegerField()),
                ("languageUnits", models.IntegerField()),
                ("fineArtsUnits", models.IntegerField()),
                ("CtaeLanguageFineArtsUnits", models.IntegerField()),
                ("healthPEUnits", models.IntegerField()),
                ("academicElectiveUnits", models.IntegerField()),
                ("freeElectiveUnits", models.IntegerField()),
                (
                    "deSchools",
                    models.ManyToManyField(
                        to="duelEnrollmentCourses.duelenrollmentschool"
                    ),
                ),
                (
                    "schoolCourses",
                    models.ManyToManyField(
                        related_name="SchoolCourses", to="courses.courses"
                    ),
                ),
                (
                    "stateID",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="State.state",
                    ),
                ),
            ],
        ),
    ]
