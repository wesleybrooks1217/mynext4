from django.shortcuts import render
from rest_framework import viewsets
from .models import  Career
import urllib.request, urllib.parse, urllib.error
import urllib.request, urllib.error, urllib.parse
import base64
import json
from django.http import JsonResponse



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
        
        careers = Career.objects.filter(name__startswith = chars)

        careers_json = {}

        counter = 0
        for career in careers:

            if counter == 5:
                break
            key = "career_" + str(counter)
            careers_json[key] = [career.name, career.onetID]
            counter += 1

        return JsonResponse(careers_json)
