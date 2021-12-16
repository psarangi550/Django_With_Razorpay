from django.db import models

# Create your models here.
class Coffee(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    amount=models.IntegerField()
    order_id=models.CharField(max_length=100,blank=True)
    paid=models.BooleanField(default=False)

    def __str__(self):
        return self.name
