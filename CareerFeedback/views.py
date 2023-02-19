from django.shortcuts import render
from .models import CareerFeedback
from Careers import models as CareerModels
from django.http import JsonResponse

# Create your views here.



class CareerFeedbackViews():

    def get_liked_careers(request, user_id):
        careers = CareerFeedback.objects.filter(userID = user_id, score__gte = 4).values('careerID', 'score')
        
        
        liked_list = []
        for career in careers:
            
            
            career_data = CareerModels.Career.objects.get(id = career["careerID"])

            temp_val = {
                "career_name": career_data.career_name,
                "onet_id": career_data.onet_id,
                "feedback": career["score"]
            }
            liked_list.append(temp_val)
            
        
        
        

        return JsonResponse({"liked_list": liked_list})


