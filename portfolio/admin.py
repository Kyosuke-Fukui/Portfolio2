from django.contrib import admin

# Register your models here.
from .models import Profile, Description, Skill, Work

admin.site.register(Profile)
admin.site.register(Description)
admin.site.register(Skill)
admin.site.register(Work)
