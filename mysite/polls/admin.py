from django.contrib import admin
from .models import ads, Question


# Register your models here.
admin.site.register(Question)
admin.site.register(ads)
