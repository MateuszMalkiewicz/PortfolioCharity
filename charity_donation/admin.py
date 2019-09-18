from django.contrib import admin
from .models import CategoryModel, InstitutionModel, DonationModel

admin.site.register(CategoryModel)
admin.site.register(InstitutionModel)
admin.site.register(DonationModel)

