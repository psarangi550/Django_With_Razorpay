from django.contrib import admin
from .models import Coffee
# Register your models here.
@admin.register(Coffee)
class CoffeeAdmin(admin.ModelAdmin):
    list_display=["id","name","email","order_id","paid"]
