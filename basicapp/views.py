from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import loginForm, signupForm
from .models import registration
# from django.contrib.gis.geoip2 import GeoIP2


def loginView(request):
    if request.method == 'GET':
        form = loginForm()
    else:
        form = loginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            print(email, password)
            if email == 'swap106111@gmail.com' and password == 'abcde':
            	return HttpResponse("LoggedIn")
    return render(request, "base.html", {'form': form})


def signupView(request):
	if request.method == 'GET':
		form = signupForm()
	else:
		form = signupForm(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']
			extra_email = form.cleaned_data['extra_email']
			print(email, password, extra_email)
			check = registration.objects.get(email=email)
			if check:
				return redirect('/signup/')
			else:
				register = registration(email= email, password=password, extra_email=extra_email)
				register.save()
				return redirect('/login/')	
			# ip = get_client_ip(request)
			# print(ip)
			# g = GeoIP2()
			# print(g.city(ip))

	return render(request, "signup.html", {'form': form})


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip