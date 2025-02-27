from django.shortcuts import render

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

def login(request):
    return render(request, 'app/login.html')

def demo(request):
    return render(request, 'app/demo.html')