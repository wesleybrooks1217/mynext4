from rest_framework import serializers
from .models import Skills, Industry, Career, States

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = (
            "id",
            'name',
            "description"
            )

class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Industry
        fields = (
            "id",
            "name",
            "icon",
            "description",
            "skills"
        )

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = (
            "id",
            "name"
        )

class CareerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Career
        fields = (
            "id",
            "industryID",
            "name",
            "dailyTasks",
            "description",
            "futureOutlook",
            "requiresCollege",
            "requiresGradSchool",
            "majorID",
            "skills", 
            "bullet_1",
            "bullet_2",
            "bullet_3",
            "bullet_4",
            "bullet_5",
            "what_they_do",
            "task_1",
            "task_2",
            "task_3",
            "knowledge_1",
            "knowledge_2",
            "knowledge_3",
            "knowledge_4",
            "knowledge_5",
            "knowledge_6",
            "skills_1",
            "skills_2",
            "skills_3",
            "skills_4",
            "skills_5",
            "abilities_1",
            "abilities_2",
            "abilities_3",
            "abilities_4",
            "abilities_5",
            "abilities_6",
            "abilities_7",
            "char_1",
            "char_2",
            "char_3",
            "char_4",
            "char_5",
            "char_6",
            "tech_1",
            "tech_2",
            "tech_3",
            "tech_4",
            "tech_5",
            "avg_degree",
            "annual_10th",
            "annual_median",
            "annual_90th",
            "hourly_10th",
            "hourly_median",
            "hourly_90th",
            "num_states_above",
            "num_states_avg",
            "num_states_below",
            "above_avg_states",
            "similar_careers",
            "industry_1_name",
            "industry_1_percent",
            "industry_2_name",
            "industry_2_percent",
            "industry_3_name",
            "industry_3_percent"
        )