from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegistrationForm, LoginForm

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('login')

def profile_view(request):
    return render(request, 'app/profile.html')

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def services(request):
    return render(request, 'app/services.html')

def careers(request):
    return render(request, 'app/careers.html')

def legal(request):
    return render(request, 'app/legal.html')

import os
from django.conf import settings

def demo(request):
    csv_path = os.path.join(settings.BASE_DIR, 'static', 'temperature_data.csv')

    # Process the CSV into a list of yearly temperature arrays
    temperature_data = []
    current_year = None
    year_data = []

    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            year = int(row['Year'])
            anomaly = float(row['Anomaly'])
            if current_year != year:
                if year_data:
                    temperature_data.append(year_data)
                year_data = []
                current_year = year
            year_data.append(anomaly)
        if year_data:  # Append the last year
            temperature_data.append(year_data)

    # Pass the data to the template
    context = {
        'temperature_data': temperature_data,
        'start_year': 1850  # Adjust based on your data
    }
    return render(request, 'app/demo.html', context)

def pricing(request):
    return render(request, 'app/pricing.html')

import json
import csv


def chart(request):
    csv_path = '/Users/crepantherx/PycharmProjects/testing.statistics.org.in/static/temperature_data.csv'

    # Process the CSV into a list of yearly temperature arrays
    temperature_data = []
    current_year = None
    year_data = []

    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            year = int(row['Year'])
            anomaly = float(row['Anomaly'])
            if current_year != year:
                if year_data:
                    temperature_data.append(year_data)
                year_data = []
                current_year = year
            year_data.append(anomaly)
        if year_data:  # Append the last year
            temperature_data.append(year_data)

    # Pass the data to the template
    context = {
        'temperature_data': temperature_data,
        'start_year': 1850  # Adjust based on your data
    }
    return render(request, 'app/chart.html', context)