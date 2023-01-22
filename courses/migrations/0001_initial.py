# Generated by Django 4.1.3 on 2023-01-13 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("resources", "0001_initial"),
        ("units", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Courses",
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
                ("name", models.CharField(default="", max_length=200)),
                ("ap", models.BooleanField(default=True)),
                ("duelEnrollment", models.BooleanField(default=True)),
                ("honors", models.BooleanField(default=True)),
                ("description", models.TextField(default="")),
                ("difficulty", models.IntegerField(default=0)),
                ("resources", models.ManyToManyField(to="resources.resources")),
                (
                    "similar_classes",
                    models.ManyToManyField(blank=True, to="courses.courses"),
                ),
                ("units", models.ManyToManyField(to="units.units")),
            ],
        ),
    ]
