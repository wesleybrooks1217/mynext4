from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.http import JsonResponse
from userAccount.models import userAccount
from Careers.models import Career
from CareerSurveyOneAnswers.models import CareerSurveyOneAnswers
from CareerSurveyOne.models import CareerSurveyOne
from CareerFeedback.models import CareerFeedback
from .models import RecommendedCareers
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity 


# Create your views here.

def recommend_careers(request, user_id):
    users = get_user_model().objects
    careers = Career.objects.all()
    answers = CareerSurveyOneAnswers.objects.all()
    questions = CareerSurveyOne.objects.all()

    user_question_matrix = np.zeros((len(users), len(questions)))

    for answer in answers:
        user_question_matrix[answer.userID - 1][answer.questionID - 1] = answer.answer

    current_user_answers = user_question_matrix[user_id - 1]
    similarity = cosine_similarity(user_question_matrix, current_user_answers.reshape(1,-1))

    similar_users = np.where(similarity[:, 0] > 0.5)
    similar_users_id = [i+1 for i in similar_users[0]]

    filtered_feedbacks = CareerFeedback.objects.filter(user__id__in=similar_users_id)
    
    user_career_matrix_filtered = np.zeros((len(similar_users[0]), len(careers)))
    for feedback in filtered_feedbacks:
        user_career_matrix_filtered[similar_users_id.index(feedback.userID)][feedback.careerID] = feedback.score

    similarity_careers = cosine_similarity(user_career_matrix_filtered)
    top_careers = np.argsort(similarity_careers[:, user_id])[::-1][:20]

    if len(top_careers) == 0:
        return HttpResponse(0)
    else:   
        for i in top_careers:
            RecommendedCareers.objects.create(userID = user_id, careerID = (i+1), similarity = similarity_careers[i, user_id])
    
        return HttpResponse(1)


def getRecommendedCareers(request, user_id):
    recommend_careers = RecommendedCareers.objects.filter(userID = user_id)
    response = []
    for career in recommend_careers:
        element = {'careerID': career.careerID, 'similarity': career.similarity}
        response.append(element)
    
    return JsonResponse(response, safe=False)


    
    

    
