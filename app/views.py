from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import RegistrationForm, LoginForm

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from .forms import RegistrationForm

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'app/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():  # This is where if form.is_valid(): belongs
            user = form.get_user()
            login(request, user)
            messages.success(request, 'Logged in successfully!')
            return redirect('home')
        else:
            # Handle unsuccessful login by adding an error message
            messages.error(request, 'Invalid username or password.')
    else:
        # For GET requests, display an empty form
        form = LoginForm()
    return render(request, 'app/login.html', {'form': form})

def logout_view(request):
    logout(request)
    # Clear any existing messages before adding the new one
    messages.get_messages(request).used = True  # Mark existing messages as used
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

from django.http import HttpResponseNotFound, HttpResponseServerError

def custom_404_view(request, exception):
    return HttpResponseNotFound('<h1>404 - Page Not Found</h1><p>The page you requested does not exist.</p>')

def custom_500_view(request):
    return HttpResponseServerError('<h1>500 - Server Error</h1><p>An error occurred on the server. Please try again later.</p>')


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