from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Sum
from charity_donation.models import DonationModel, InstitutionModel, CategoryModel
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
        if request.user.is_authenticated:
            context = {'categories': CategoryModel.objects.all(),
                       'institutions': InstitutionModel.objects.all(),
                       }
            return render(request, 'form.html', context)
        else:
            return redirect('/login')

    def post(self, request):
        institution = InstitutionModel.objects.filter(id=request.POST['institution'])
        # donation = DonationModel.objects.create(bag_quantity=request.POST['bags'],
        #                                         categories=request.POST['categories'],
        #                                         institution=institution,
        #                                         address=request.POST['address'],
        #                                         phone_number=request.POST['phone'],
        #                                         city=request.POST['city'],
        #                                         zip_code=request.POST['postcode'],
        #                                         pick_up_date=request.POST['data'],
        #                                         pick_up_time=request.POST['time'],
        #                                         pick_up_comment=request.POST['more_info'],
        #                                         user=request.user)
        # donation.save()
        # return redirect('/', {'confirmed': True})
        return render(request, 'test.html', {'inst': institution})


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
            return redirect('/register/#register-form')


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
        return redirect('/')


class ProfileView(View):
    def get(self, request):
        context = {'donations': DonationModel.objects.filter(user=request.user).order_by('is_taken')}
        return render(request, 'user-panel.html', context)


class ArchiveDonationView(View):
    def get(self, request, donation_id):
        donation = DonationModel.objects.get(id=donation_id)
        donation.is_taken = True
        donation.save()
        return redirect('/profile')
