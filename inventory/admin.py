from django.contrib import admin
from inventory.models import Hospital, Department, Item

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Department)
admin.site.register(Item)
