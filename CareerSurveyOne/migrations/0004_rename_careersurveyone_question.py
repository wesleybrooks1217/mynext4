# Generated by Django 4.1 on 2023-01-31 01:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        (
            "CareerSurveyOneAnswers",
            "0002_rename_survey_careersurveyoneanswers_questionid_and_more",
        ),
        ("CareerSurveyOne", "0003_remove_careersurveyone_favorite_careers_and_more"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="CareerSurveyOne",
            new_name="Question",
        ),
    ]
