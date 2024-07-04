from django.urls import path
from . import views

urlpatterns = [
    path('sign-in/', views.sign_in, name='sign_in'),
    path('sign-up/', views.sign_up, name='sign_up'),
    path('sign-out/', views.sign_out, name='sign_out'),
    path('logout/', views.sign_out, name='logout'),
    path('reset-password/', views.reset_password, name='reset_password'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('lock-screen/', views.lock_screen, name='lock_screen'),
    path('2FA/', views.two_fa, name='two_fa'),
]
