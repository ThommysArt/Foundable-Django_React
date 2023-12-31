"""Foundable URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/freelance', include('freelance.urls')),
    path('api/v1/marketplace', include('marketplace.urls')),
    path('api/v1/membership', include('membership.urls')),
    path('api/v1/startup', include('startup.urls')),
    path('api/v1/subscriptions', include('subscriptions.urls')),
    path('api/v1/transactions', include('transactions.urls')),
]
