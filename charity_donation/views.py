from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Sum
from charity_donation.models import DonationModel, InstitutionModel
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


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

    def post(self, request):
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'register.html', {'not_registered': True})


class RegisterView(View):
    def verify(self, *args):
        valid = True
        for item in args:
            if item is None or len(item) == 0:
                valid = False
        return valid

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        name = request.POST['name']
        surname = request.POST['surname']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2 and self.verify(name, surname, email, password, password2):
            User.objects.create_user(username=email, first_name=name, last_name=surname,
                                     email=email, password=password)
            return render(request, 'login.html')
        return render(request, 'register.html', {'incorrect': True})


class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, 'index.html')
