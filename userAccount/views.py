from django.shortcuts import render
from rest_framework import viewsets
from .serializers import AccomplishmentsSerializer, UserSerializer
from .models import Accomplishments, AbstractBaseUser, MyAccountManager
from django.contrib.auth import get_user_model
from rest_framework.permissions import AllowAny
import string
import random
from Careers.models import Career
from CareerFeedback.models import CareerFeedback
from django.http import HttpResponse


class AccomplishmentsView(viewsets.ModelViewSet):
    serializer_class = AccomplishmentsSerializer
    queryset = Accomplishments.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = get_user_model().objects

    def get_permissions(self):
        if self.request.method == 'POST':
            self.permission_classes = (AllowAny, )
        return super(UserViewSet, self).get_permissions()
    
    


# Create your views here.
def create_fake_users(request):


    for i in range(25):
        email, password, username = random_email_and_password_and_username()

        user_id = MyAccountManager.simulat_user_create(email = email, username =username, password = password)
        ##user_id = user.get_id()
        for _ in range(25):
            set_feedback_careers(user_id)
    return HttpResponse({"Success"})



def random_email_and_password_and_username():
    
    random_email = '.'.join(random.choice(string.ascii_lowercase) for _ in range(10))
    random_email += "&gamil.com"

    random_password = '.'.join(random.choice(string.ascii_lowercase) for _ in range(10))
    random_username = '.'.join(random.choice(string.ascii_lowercase) for _ in range(10))
    return random_email, random_password, random_username



def set_feedback_careers(user_id):
    careers = list(Career.objects.all())
    num_careers = len(careers)
    rand_career = random.randint(0, num_careers)
    rand_rating = random.random() * 5
    _, created = CareerFeedback.objects.get_or_create(
        userID = user_id,
        careerID = rand_career,
        score = rand_rating
    )





