from django.shortcuts import render
from rest_framework import viewsets
from .models import  Career
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import base64
import json
from django.http import JsonResponse
from courses import models as CoursesMod
import csv

# Create your views here.


class CareerViews():

    def call_onet(request, onet_id):
        headers = {
            'User-Agent': 'python-OnetWebService/1.00 (bot)',
            'Authorization': 'Basic ' + base64.standard_b64encode(("linkedin_company_myn" + ':' + "5725apz").encode()).decode(),
            'Accept': 'application/json' 
                        }
        
        url = "https://services.onetcenter.org/ws/mnm/careers/" + str(onet_id) + "/report"

        req = urllib.request.Request(url, None, headers)
        handle = urllib.request.urlopen(req) 
        return JsonResponse(json.load(handle))


    def career_serach(request, chars):
        
        careers = Career.objects.filter(career_name__startswith = chars)

        careers_list = []

        counter = 0
        for career in careers:

            if counter == 5:
                break

            careers_list.append({
                "career_name": career.career_name,
                "onet_id": career.onet_id
            })
            
            
            counter += 1

        return JsonResponse({"careers": careers_list})
    
        
    

    def career_filter(request):
        
        careers_business = Career.objects.filter(industry = "Business").values('career_name', 'onet_id')
        careers_agriculture = Career.objects.filter(industry = "Agriculture").values('career_name', 'onet_id')
        careers_manufacturing = Career.objects.filter(industry = "Manufacturing").values('career_name', 'onet_id')
        careers_health = Career.objects.filter(industry = "Health").values('career_name', 'onet_id')
        careers_engineering = Career.objects.filter(industry = "Engineering").values('career_name', 'onet_id')
        careers_human_resources = Career.objects.filter(industry = "Human Resources").values('career_name', 'onet_id')
        careers_30000 = Career.objects.filter(median_salary__gt = 30000).values('career_name', 'onet_id')
        careers_50000 = Career.objects.filter(median_salary__gt = 50000).values('career_name', 'onet_id')
        careers_75000 = Career.objects.filter(median_salary__gt = 75000).values('career_name', 'onet_id')
        careers_100000 = Career.objects.filter(median_salary__gt = 100000).values('career_name', 'onet_id')
        careers_125000 = Career.objects.filter(median_salary__gt = 125000).values('career_name', 'onet_id')
        careers_high_school = Career.objects.filter(education = "HighSchool").values('career_name', 'onet_id')
        careers_bachelors = Career.objects.filter(education = "Bachelors").values('career_name', 'onet_id')
        careers_masters = Career.objects.filter(education = "Masters").values('career_name', 'onet_id')
        careers_doctorate = Career.objects.filter(education = "Doctorate").values('career_name', 'onet_id')

        return JsonResponse({
            'business': list(careers_business),
            'agriculture': list(careers_agriculture),
            'manufacturing': list(careers_manufacturing),
            'health': list(careers_health),
            'engineering': list(careers_engineering),
            'human_resources': list(careers_human_resources),
            'thirty_thousand': list(careers_30000),
            'fifty_thousand': list(careers_50000),
            'seventyfive_thousand': list(careers_75000),
            'onehundred_thousand': list(careers_100000),
            'onehundredtwentyfive_thousand': list(careers_125000),
            'high_school': list(careers_high_school),
            'bachelors': list(careers_bachelors),
            'masters': list(careers_masters),
            'doctorate': list(careers_doctorate)
        })
    
    

    def career_filter_industry(request, industryIn):
        
        careers = Career.objects.filter(industry = industryIn).values('career_name', 'onet_id')
        return JsonResponse({'careers': list(careers)})
    

    def career_filter_salary(request, salaryIn):
        
        careers = Career.objects.filter(median_salary__gt = salaryIn).values('career_name', 'onet_id')

        return JsonResponse({'careers': list(careers)})

    def career_filter_education(request, education):

        careers = Career.objects.filter(education = education).values('career_name', 'onet_id')

        return JsonResponse({'careers': list(careers)})
    

    def load_careers(request):
    
    
    ##with codecs.open("Careers.xlsx", 'r', encoding='utf-8', errors='ignore') as f:
        
        with open("Careers.csv", 'rt') as f:
            reader = csv.reader(f)
            
            
            for row in reader:
                break

            counter = 0
            
            for row in reader:
                
                _, created = Career.objects.get_or_create(
                    career_name = row[0],
                    onet_id = row[1],
                    median_salary = int(row[2]),
                    industry = row[3],
                    education = row[4]
                )
    
