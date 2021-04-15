from django.db import models
from django.contrib.auth.models import User

class LgsiExam(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    question = models.CharField(max_length=500, default='')
    option1 = models.CharField(max_length=200, default='')
    option2 = models.CharField(max_length=200, default='')
    option3 = models.CharField(max_length=200, default='')
    option4 = models.CharField(max_length=200, default='')
    answer = models.CharField(max_length=200, default='')
    examtype = models.CharField(max_length=20, default='')
    
    def __str__(self):
        return str(self.question)


class UserAnswer(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    exam_number = models.IntegerField(default=0)
    result = models.CharField(max_length=200, default='')
    examtype = models.CharField(max_length=200, default='')

    def __str__(self):
        return str(self.user)

class UserEmpId(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    emp_id = models.CharField(max_length=200, default='')

    def __str__(self):
        return str(self.emp_id)
        
