from django.shortcuts import render
from rest_framework import viewsets
from .serializers import CollegeSerializer
from .models import College
from django.http import JsonResponse


# Create your views here.

class CollegeView():
    
    def filter_acceptance_rate(request, rate):
        colleges = College.objects.filter(acceptance_rate__gt = rate).values("name", "collegeAIKey")
        return JsonResponse({"colleges": list(colleges)})
    
    def filter_sat_score(request, score):
        colleges = College.objects.filter(sat_score__gt = score).values("name", "collegeAIKey")
        return JsonResponse({"colleges": list(colleges)})
    
    def filter_average_fin_aid(request, aid):
        colleges = College.objects.filter(average_fin_aid__gt = aid).values("name", "collegeAIKey")
        return JsonResponse({"colleges": list(colleges)})
    
    def filter_ten_year_earnings(request, aid):
        colleges = College.objects.filter(ten_year_earnings__gt = aid).values("name", "collegeAIKey")
        return JsonResponse({"colleges": list(colleges)})
    
    def college_serach(request, chars):
        
        colleges = College.objects.filter(name__startswith = chars)

        colleges_list = []

        counter = 0
        for college in colleges:

            if counter == 5:
                break

            colleges_list.append({
                "college_name": college.name,
                "collegeAIKey": college.collegeAIKey
            })
            
            
            counter += 1

        return JsonResponse({"careers": colleges_list})
