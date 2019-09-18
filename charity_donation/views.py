from django.shortcuts import render
from django.views import View
from django.db.models import Sum, Count
from charity_donation.models import DonationModel


class LandingPageView(View):
    def get(self, request):
        donations = DonationModel.objects.all()
        institutions = DonationModel.objects.values('institution').distinct()
        context = {'sum_of_bags': donations.aggregate(Sum('bag_quantity')),
                   'sum_of_institutions':  institutions.count()
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
