# Generated by Django 4.1.3 on 2023-01-13 17:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("courses", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="RecommendedCourses",
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
                ("similarityScore", models.FloatField(null=True)),
                (
                    "courseID",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="CourseID",
                        to="courses.courses",
                    ),
                ),
                (
                    "userID",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="UserID",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
