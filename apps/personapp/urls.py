from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                    # homepage
    path('persons/', views.person_list, name='person_list'),
    # add more routes later...
]
