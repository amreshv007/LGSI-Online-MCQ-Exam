from django.contrib import admin
from .models import LgsiExam, UserAnswer, UserEmpId
# Register your models here.

admin.site.register(LgsiExam)
admin.site.register(UserAnswer)
admin.site.register(UserEmpId)