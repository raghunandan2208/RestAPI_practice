"""bankproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('country_list/', views.country_list),
    path('user_list/', views.user_list),
    path('referal_list/', views.referal_list),
    path('state_list/', views.state_list),
    path('bank_list/', views.bank_list),
    path('gender_list/', views.gender_list),
    path('document_list/', views.document_list),
]
