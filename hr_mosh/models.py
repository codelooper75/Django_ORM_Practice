from django.db import models


class Offices(models.Model):
    #office_id = pk
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.address} {self.city} / {self.state}"



class Employees(models.Model):
    #employee_id = pk
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    salary = models.IntegerField()
    reporst_to = models.ForeignKey("Employees", on_delete=models.SET_NULL, null=True, blank=True)
    office = models.ForeignKey(Offices, on_delete=models.SET_NULL, null=True, blank=True )

    def __str__(self):
        return f"{self.first_name} {self.last_name} / {self.job_title}"