from django.shortcuts import render
from django.contrib.auth import get_user_model
from userAccount.models import userAccount
from Careers.models import Career
from CareerSurveyOneAnswers.models import CareerSurveyOneAnswers
from CareerSurveyOne.models import CareerSurveyOne


# Create your views here.
"""
def recommend_careers(request, user_id):
    current_user = get_user_model()
    users = get_user_model().objects
    careers = Career.objects.all()
    answers = CareerSurveyOneAnswers.objects.all()
    questions = CareerSurveyOne.objects.all()

    user_question_matrix = np.zeros((len(users), len(questions)))

    for answer in answers:
        user_question_matrix[answer.userID - 1][answer.questionID - 1] = answer.answer

    current_user_answers = user_question_matrix[current_user.id - 1]
    similarity = cosine_similarity(user_question_matrix, current_user_answers.reshape(1,-1))

    similar_users = np.where(similarity[:, 0] > 0.5)
    similar_users_id = [i+1 for i in similar_users[0]]
"""
    

    
