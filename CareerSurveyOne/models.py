from django.db import models

# Create your models here.

class Question(models.Model):
    question = models.CharField(max_length=100, default='')
    def __str__(self):
        return self.question
    """       
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
        (0, 'Mathematics'),
        (1, 'History'),
        (2, 'Sciences'),
        (3, 'English & Literature'),
        (4, 'Humanities & Arts'),
    )
    favorite_subject = models.IntegerField(choices=FAVORITE_SUBJECT)
    FAVORITE_CAREERS = (
        (0, 'Business and finance'),
        (1, 'Healthcare and science'),
        (2, 'Education and social services'),
        (3, 'Manufacturing, construction and engineering'),
        (4, 'Media, arts, and entertainment'),
        (5, 'Retail, hospitality, and tourism'),
    )
    favorite_careers = models.IntegerField(choices=FAVORITE_CAREERS)
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
"""        