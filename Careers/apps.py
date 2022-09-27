from django.apps import AppConfig


class CareersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Career'

class SkillsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Skills'

class IndustrysConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Industry'

