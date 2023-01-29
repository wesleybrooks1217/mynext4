from django.db import models
from django.conf import settings
from CareerSurveyOne.models import CareerSurveyOne

# Create your models here.
AUTH_USER_MODEL = settings.AUTH_USER_MODEL

class CareerSurveyOneAnswers(models.Model):
    survey = models.ForeignKey(CareerSurveyOne, on_delete=models.CASCADE)
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    answer = models.IntegerField()
    
    def generate_secondary_school_answers(self, survey_id, user_id):
        survey = CareerSurveyOne.objects.get(id=survey_id)
        user = AUTH_USER_MODEL.objects.get(id=user_id)
        question = 'Do you have a desire to attend a college, university, or other secondary education?'
        answer = survey.secondary_school
        CareerSurveyOneAnswers.objects.create(survey=survey, user=user, question=question, answer=answer)
    def generate_tertiary_school_answers(self, survey_id, user_id):   
        survey = CareerSurveyOne.objects.get(id=survey_id)
        user = AUTH_USER_MODEL.objects.get(id=user_id)
        question = 'Do you have a desire to attend school after university? (Law School, Medical School, Masters, etc)'
        answer = survey.tertiary_school
        CareerSurveyOneAnswers.objects.create(survey=survey, user=user, question=question, answer=answer)
    def generate_independent_job_answers(self, survey_id, user_id):   
        survey = CareerSurveyOne.objects.get(id=survey_id)
        user = AUTH_USER_MODEL.objects.get(id=user_id)
        question = 'Would you rather work alone on assignments over a team?'
        answer = survey.independent_school
        CareerSurveyOneAnswers.objects.create(survey=survey, user=user, question=question, answer=answer)    
    def generate_work_from_home_answers(self, survey_id, user_id):   
        survey = CareerSurveyOne.objects.get(id=survey_id)
        user = AUTH_USER_MODEL.objects.get(id=user_id)
        question = 'Would you rather work from home than in the office?'
        answer = survey.work_from_home
        CareerSurveyOneAnswers.objects.create(survey=survey, user=user, question=question, answer=answer)    
    def generate_favorite_subject_answers(self, survey_id, user_id):   
        survey = CareerSurveyOne.objects.get(id=survey_id)
        user = AUTH_USER_MODEL.objects.get(id=user_id)
        question = 'What is your favorite subject in school?'
        answer = getattr(survey, 'favorite_subject')
        CareerSurveyOneAnswers.objects.create(survey=survey, user=user, question=question, answer=answer)    
    def generate_favorite_career_answers(self, survey_id, user_id):   
        survey = CareerSurveyOne.objects.get(id=survey_id)
        user = AUTH_USER_MODEL.objects.get(id=user_id)
        question = 'Which career sector seems suitable for you?'
        answer = getattr(survey, 'favorite_careers')
        CareerSurveyOneAnswers.objects.create(survey=survey, user=user, question=question, answer=answer)    
    def generate_shifting_schedule_answers(self, survey_id, user_id):   
        survey = CareerSurveyOne.objects.get(id=survey_id)
        user = AUTH_USER_MODEL.objects.get(id=user_id)
        question = 'Would you prefer a flexible schedule over the general 40 hour work week?'
        answer = survey.shifting_schedule
        CareerSurveyOneAnswers.objects.create(survey=survey, user=user, question=question, answer=answer)    
    def generate_socializing_more_answers(self, survey_id, user_id):   
        survey = CareerSurveyOne.objects.get(id=survey_id)
        user = AUTH_USER_MODEL.objects.get(id=user_id)
        question = 'Would you prefer to have more socializing than silence?'
        answer = survey.socializing_more
        CareerSurveyOneAnswers.objects.create(survey=survey, user=user, question=question, answer=answer) 
    def generate_sports_as_career_answers(self, survey_id, user_id):   
        survey = CareerSurveyOne.objects.get(id=survey_id)
        user = AUTH_USER_MODEL.objects.get(id=user_id)
        question = 'Are you interested in becoming a professional athlete?'
        answer = survey.sports_as_career
        CareerSurveyOneAnswers.objects.create(survey=survey, user=user, question=question, answer=answer)           
    def generate_travel_for_work_answers(self, survey_id, user_id):   
        survey = CareerSurveyOne.objects.get(id=survey_id)
        user = AUTH_USER_MODEL.objects.get(id=user_id)
        question = 'Would you want to travel for work?'
        answer = survey.travel_for_work
        CareerSurveyOneAnswers.objects.create(survey=survey, user=user, question=question, answer=answer)            