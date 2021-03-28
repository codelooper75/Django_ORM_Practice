from django.db import models

# Create your models here.
class Customers(models.Model):
    #employee_id = pk
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birth_date = models.DateField()
    phone = models.CharField(max_length=100)
    adress = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    points = models.IntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name} / {self.state}"

class Shippers(models.Model):
    #shipper_id
    name = models.CharField(max_length=200)

class Orders(models.Model):
    #order_id
    customer = models.ForeignKey(Customers, on_delete=models.SET_NULL, null=True, blank=True)
    order_date = models.DateField()
    status = models.IntegerField()
    comments = models.CharField(max_length=2000)
    shipped_date = models.DateField()
    shipper = models.ForeignKey(Shippers, on_delete=models.SET_NULL, null=True, blank=True)




class Order_item_notes(models.Model):
    order = models.ForeignKey(Orders, on_delete=models.CASCADE, null=True)