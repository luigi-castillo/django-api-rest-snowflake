from django.db import models


# Create your models here.
class Departments(models.Model):
    id = models.IntegerField(primary_key=True)
    department = models.TextField(null=True)


class Jobs(models.Model):
    id = models.IntegerField(primary_key=True)
    job = models.TextField(null=True)


class HiredEmployees(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField(null=True)
    datetime = models.DateTimeField(null=True)
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Jobs, on_delete=models.CASCADE)
