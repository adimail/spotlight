from django.shortcuts import render, HttpResponse

# Create your views here.

def index_view(request):
    return render(request, 'index.html', {'page_title': 'Home'})

def about_view(request):
    return render(request, 'about.html', {'page_title': 'About Us'})

def contact_view(request):
    return render(request, 'contact.html', {'page_title': 'Contact Us'})