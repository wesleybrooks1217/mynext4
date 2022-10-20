from re import U
from rest_framework import serializers
from .models import Accomplishments, AbstractBaseUser
from django.contrib.auth import get_user_model
from djoser.serializers import UserCreateSerializer

User = get_user_model()

class AccomplishmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Accomplishments
        fields = (
            'id',
            'name',
            'leadership',
            'schoolAward',
            'stateAward',
            'nationalAward',
            'competition'
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'username',
            'date_joined',
            'last_login',
            'is_admin',
            'is_active',
            'is_staff',
            'is_superuser',
            'school',
            'firstName',
            'lastName',
            'year',
            'desiredIndustry',
            'wantsCollege',
            'gpa',
            'numHonorsClasses',
            'numAPClasses',
            'numIBClasses',
            'numDEClasses',
            'familyIncome',
            'maxSpending',
            'sat',
            'satAttempts',
            'act',
            'accomplishments',
            'prevCourses',
            'likedSchools',
            'likedCareers'
        )


class AccountUserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'name', 'password')