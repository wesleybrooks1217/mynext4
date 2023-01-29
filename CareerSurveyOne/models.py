from django.db import models

# Create your models here.

class CareerSurveyOne(models.Model):
    SECONDARY_SCHOOL = (
        (0, 'No'),
        (1, 'Yes'),
    )
    secondary_school = models.IntegerField(choices=SECONDARY_SCHOOL)
    TERTIARY_SCHOOL = (
        (0, 'No'),
        (1, 'Yes'),
    )
    tertiary_school = models.IntegerField(choices=TERTIARY_SCHOOL)
    INDEPENDENT_JOB = (
        (0, 'No'),
        (1, 'Yes'),
    )
    independent_job = models.IntegerField(choices=INDEPENDENT_JOB)
    WORK_FROM_HOME = (
        (0, 'No'),
        (1, 'Yes'),
    )
    work_from_home = models.IntegerField(choices=WORK_FROM_HOME)
    FAVORITE_SUBJECT = (
        ('MTH', 'Mathematics'),
        ('HIS', 'History'),
        ('SCI', 'Sciences'),
        ('ENG', 'English & Literature'),
        ('ART', 'Humanities & Arts'),
    )
    favorite_subject = models.CharField(max_length=3, choices=FAVORITE_SUBJECT)
    FAVORITE_CAREERS = (
        ('BF', 'Business and finance'),
        ('HS', 'Healthcare and science'),
        ('ESS', 'Education and social services'),
        ('MCE', 'Manufacturing, construction and engineering'),
        ('MAE', 'Media, arts, and entertainment'),
        ('RHT', 'Retail, hospitality, and tourism'),
    )
    favorite_careers = models.CharField(max_length=3, choices=FAVORITE_CAREERS)
    SHIFTING_SCHEDULE = (
        (0, 'No'),
        (1, 'Yes'),
    )
    shifting_schedule = models.IntegerField(choices=SHIFTING_SCHEDULE)
    SOCIALIZING_MORE = (
        (0, 'No'),
        (1, 'Yes'),
    )
    socializing_more = models.IntegerField(choices=SOCIALIZING_MORE)
    SPORTS_AS_CAREER = (
        (0, 'No'),
        (1, 'Yes'),
    )
    sports_as_career = models.IntegerField(choices=SPORTS_AS_CAREER)
    TRAVEL_FOR_WORK = (
        (0, 'No'),
        (1, 'Yes')
    )
    travel_for_work = models.IntegerField(choices=TRAVEL_FOR_WORK)

