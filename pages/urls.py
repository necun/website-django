from django.urls import path

from . import views

handler404 = 'pages.views.custom_404'

urlpatterns = [
    path('', views.index, name='index'),
    path('products/', views.products, name='products'),
    path('welcome/', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('privacy-policy-2/', views.privacy_policy, name='privacy_policy'),
    path('services-agency/', views.terms, name='terms'),
]
