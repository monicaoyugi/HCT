from django.contrib import admin
from inventory.models import Hospital, Item, Donor

# Register your models here.
admin.site.register(Hospital)
admin.site.register(Item)
admin.site.register(Donor)
