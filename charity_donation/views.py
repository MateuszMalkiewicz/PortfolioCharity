from django.shortcuts import render
from django.views import View
from django.db.models import Sum, Count
from charity_donation.models import DonationModel, InstitutionModel


class LandingPageView(View):
    def get(self, request):
        donations = DonationModel.objects.all()
        institutions_supported = DonationModel.objects.values('institution').distinct()

        context = {
                   'sum_of_bags': donations.aggregate(Sum('bag_quantity')),
                   'sum_of_institutions_supported':  institutions_supported.count(),
                   'foundations': InstitutionModel.objects.filter(type='fund'),
                   'organizations': InstitutionModel.objects.filter(type='org'),
                   'local': InstitutionModel.objects.filter(type='local')
                   }

        return render(request, 'index.html', context)


class AddDonationView(View):
    def get(self, request):
        return render(request, 'form.html')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')


class RegisterView(View):
    def get(self, request):
        return render(request, 'register.html')
