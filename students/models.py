from django.db import models


class Student(models.Model):
    student_name = models.CharField(max_length=30)
    reg_no = models.CharField(max_length=5)
    course = models.CharField(max_length=10)
    date_joined = models.DateField()
    level = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.student_name}: {self.reg_no}"
