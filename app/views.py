from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'index.html', {})

def donate(request):

    return render(request, 'donate.html', {})

def contact(request):

    return render(request, 'contact.html')

def about(request):

    return render(request, 'about.html')

def looking(request):

    return render(request, 'looking.html')