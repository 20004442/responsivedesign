from django.shortcuts import render

# Create your views here.

def home(request):
    context = {}
    return render(request, 'mydesign/home.html', context)
    
def productsresponsive(request):
    context = {}
    return render(request, 'mydesign/productsresponsive.html', context)
    
def peopleresponsive(request):
    context = {}
    return render(request, 'mydesign/peopleresponsive.html', context)

def contactus(request):
    context = {}
    return render(request, 'mydesign/contactus.html', context)