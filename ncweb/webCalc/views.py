from django.shortcuts import render

def index(request):
    return render(request, 'webCalc/index.html', context={})

def calculator(request):
    return render(request, 'webCalc/calculator.html', context={})
# Create your views here.
