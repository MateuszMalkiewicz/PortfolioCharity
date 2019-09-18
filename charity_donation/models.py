from django.db import models
from django.contrib.auth.models import User


TYPES = {
    ('fund', 'fundacja'),
    ('org', 'organizacja pozarządowa'),
    ('local', 'zbiórka lokalna'),
}


class CategoryModel(models.Model):
    name = models.CharField(max_length=128)


class InstitutionModel(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField()
    type = models.CharField(choices=TYPES, default='fund', max_length=6)
    categories = models.ManyToManyField(CategoryModel)


class DonationModel(models.Model):
    quantity = models.IntegerField()
    categories = models.ManyToManyField(CategoryModel)
    institution = models.ForeignKey(InstitutionModel, on_delete=models.DO_NOTHING)
    address = models.TextField()
    phone_number = models.CharField(max_length=16)
    city = models.CharField(max_length=64)
    zip_code = models.CharField(max_length=6)
    pick_up_date = models.DateField()
    pick_up_time = models.TimeField()
    pick_up_comment = models.TextField()
    user = models.ForeignKey(User, null=True, default=None, on_delete=models.DO_NOTHING)
