from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def products(request):
    return render(request, 'products.html')

def app(request):
    return render(request, 'app.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')

def checkout(request):
    return render(request, 'checkout.html')

def thankyou(request):
    return render(request, 'thankyou.html')


def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def terms(request):
    return render(request, 'terms.html')