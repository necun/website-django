from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('app/', views.app, name='app'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('privacy-policy-2/', views.privacy_policy, name='privacy_policy'),
    path('services-agency/', views.terms, name='terms'),
]
