# from django.shortcuts import render
# from django.contrib.auth import get_user_model
# from django.http import HttpResponse
# from django.http import JsonResponse
# from userAccount.models import userAccount
# from Careers.models import Career
# from CareerSurveyOneAnswers.models import CareerSurveyOneAnswers
# from CareerSurveyOne.models import Question
# from CareerFeedback.models import CareerFeedback
# from .models import RecommendedCareers
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity 


# # Create your views here.


# class RecommendedCareersViews:

#     def recommend_careers(user_id):
#         users = userAccount.objects.all()
#         careers = Career.objects.all()
#         answers = CareerSurveyOneAnswers.objects.all()
#         questions = Question.objects.all()

#         user_question_matrix = np.zeros((len(users), len(questions)))

#         for answer in answers:
#             user_question_matrix[answer.userID - 1][answer.questionID - 1] = answer.answer

#         current_user_answers = user_question_matrix[user_id - 1]
#         similarity = cosine_similarity(user_question_matrix, current_user_answers.reshape(1,-1))

#         similar_users = np.where(similarity[:, 0] > 0.5)
#         similar_users_id = [i+1 for i in similar_users[0]]

#         filtered_feedbacks = CareerFeedback.objects.filter(user__id__in=similar_users_id)
        
#         user_career_matrix_filtered = np.zeros((len(similar_users[0]), len(careers)))
#         for feedback in filtered_feedbacks:
#             user_career_matrix_filtered[similar_users_id.index(feedback.userID)][feedback.careerID] = feedback.score

#         similarity_careers = cosine_similarity(user_career_matrix_filtered)
#         top_careers = np.argsort(similarity_careers[:, user_id])[::-1][:20]

        
#         for i in top_careers:
#             RecommendedCareers.objects.create(userID = user_id, careerID = (i+1), similarity = similarity_careers[i, user_id])
        
            


#     def getRecommendedCareers(request, user_id):
#         recommended_careers = RecommendedCareers.objects.filter(userID = user_id)
#         if (len(recommended_careers) == 0):
#             RecommendedCareersViews.recommend_careers(user_id)
#             recommended_careers = RecommendedCareers.objects.filter(userID = user_id)
        
#         response = []
#         for rec_career in recommended_careers:
#             career = Career.objects.get(id = rec_career.careerID)
#             element = {'career_name': career.career_name, 'similarity': rec_career.similarity, 'onet_id': career.onet_id}
#             response.append(element)
        
        

        
#         return JsonResponse({'careers': response})


    
    

    
