"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from django.views.generic import TemplateView

from college import views as collegeView
from Careers import views as CareersView
from duelEnrollmentCourses import views as duelEnrollmentCoursesView
from State import views as stateView
from School import views as schoolView
from userAccount import views as userAccountView
from CareerSurveyOne import views as careerSurveyOneView
from CareerSurveyOneAnswers import views as careerSurveyOneAnswersView
from RecommendedCareers import views as recommendedCareersViews
from CareerFeedback import views as CareerFeedbackViews

router = routers.DefaultRouter()
router.register(r'colleges', collegeView.CollegeView, 'college')


router.register(r'duelEnrollmentCourses', duelEnrollmentCoursesView.duelEnrollmentCoursesView, 
                'duelEnrollmentCourses')
router.register(r'duelEnrollmentSchool', duelEnrollmentCoursesView.duelEnrollmentSchoolView,
                'duelEnrollmentSchool')
router.register(r'State', stateView.StateView, 'State')
router.register(r'School', schoolView.SchoolView, 'School')
router.register(r'Accomplishment', userAccountView.AccomplishmentsView,
                'Accomplishment')
router.register(r'User', userAccountView.UserViewSet, 'User')
router.register(r'CareerSurveyOne', careerSurveyOneView.CareerSurveyOneView , 'CareerSurveyOne')
router.register(r'CareerSurveyOneAnswers', careerSurveyOneAnswersView.CareerSurveyOneAnswersView, 'CareerSurveyOneAnswers')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/survey/', include('CareerSurveyOne.urls')),
    path('recommendations/create/careers', recommendedCareersViews.RecommendedCareersViews.recommend_careers),
    path('api/career/<str:onet_id>/', CareersView.CareerViews.call_onet),
    path('api/search/career/<str:chars>/', CareersView.CareerViews.career_serach),
    path('api/explore/career/salary/<int:salaryIn>/', CareersView.CareerViews.career_filter_salary),
    path('api/explore/career/industry/<str:industryIn>/', CareersView.CareerViews.career_filter_industry),
    path('api/explore/career/course/<str:course_name>/', CareersView.CareerViews.career_filter_course),
    path('api/users/careerlist/<int:user_id>/', CareerFeedbackViews.CareerFeedbackViews.get_liked_careers),
    path('api/explore/career/', CareersView.CareerViews.career_filter),
    path('api/users/careerlist/add/', CareerFeedbackViews.CareerFeedbackViews.add_career_feedback),
    
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name = 'index.html'))]
