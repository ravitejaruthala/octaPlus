from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'mudra/home.html')

def signup(request):
    return render(request, 'mudra/signup.html')

def login(request):
    return render(request, 'mudra/login.html')
