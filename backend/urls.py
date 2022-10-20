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
from highSchoolCourses import views as highSchoolCoursesView
from Careers import views as CareersView
from duelEnrollmentCourses import views as duelEnrollmentCoursesView
from State import views as stateView
from School import views as schoolView
from userAccount import views as userAcccountView



router = routers.DefaultRouter()
router.register(r'colleges', collegeView.CollegeView, 'college')
router.register(r'highSchoolCourses', highSchoolCoursesView.highSchoolCoursesView,
                'highSchoolCourses')
router.register(r'skills', CareersView.SkillsView, 'skills')
router.register(r'industry', CareersView.IndustryView, 'industry')
router.register(r'career', CareersView.CareerView, 'career')
router.register(r'duelEnrollmentCourses', duelEnrollmentCoursesView.duelEnrollmentCoursesView, 
                'duelEnrollmentCourses')
router.register(r'duelEnrollmentSchool', duelEnrollmentCoursesView.duelEnrollmentSchoolView,
                'duelEnrollmentSchool')
router.register(r'State', stateView.StateView, 'State')
router.register(r'School', schoolView.SchoolView, 'School')
router.register(r'Accomplishment', userAcccountView.AccomplishmentsView,
                'Accomplishment')
router.register(r'User', userAcccountView.UserViewSet, 'User')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name = 'index.html'))]
