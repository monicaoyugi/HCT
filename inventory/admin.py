from django.contrib import admin
from inventory.models import Hospital, ItemDonated, Donor

# Register your models here.
admin.site.register(Hospital)
admin.site.register(ItemDonated)
admin.site.register(Donor)
