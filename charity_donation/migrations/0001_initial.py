# Generated by Django 2.2.5 on 2019-09-22 16:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='InstitutionModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('local', 'zbiórka lokalna'), ('fund', 'fundacja'), ('org', 'organizacja pozarządowa')], default='fund', max_length=6)),
                ('categories', models.ManyToManyField(to='charity_donation.CategoryModel')),
            ],
        ),
        migrations.CreateModel(
            name='DonationModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bag_quantity', models.IntegerField()),
                ('address', models.TextField()),
                ('phone_number', models.CharField(max_length=16)),
                ('city', models.CharField(max_length=64)),
                ('zip_code', models.CharField(max_length=6)),
                ('pick_up_date', models.DateField()),
                ('pick_up_time', models.TimeField()),
                ('pick_up_comment', models.TextField()),
                ('categories', models.ManyToManyField(to='charity_donation.CategoryModel')),
                ('institution', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='charity_donation.InstitutionModel')),
                ('user', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
