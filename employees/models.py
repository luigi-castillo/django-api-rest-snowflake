from django.db import models


# Create your models here.
class Departments(models.Model):
    id = models.IntegerField(primary_key=True)
    department = models.TextField()


class Jobs(models.Model):
    id = models.IntegerField(primary_key=True)
    job = models.TextField()


class HiredEmployees(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    datetime = models.TextField()
    department_id = models.ForeignKey(Departments, on_delete=models.CASCADE)
    job_id = models.ForeignKey(Jobs, on_delete=models.CASCADE)


class DepartmentsRejected(models.Model):
    department_id = models.IntegerField()
    department = models.TextField()


class JobsRejected(models.Model):
    job_id = models.IntegerField()
    job = models.TextField()


class HiredEmployeesRejected(models.Model):
    hired_employee_id = models.IntegerField()
    name = models.TextField()
    datetime = models.TextField()
    department_id = models.IntegerField()
    job_id = models.IntegerField()

