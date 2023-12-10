from django.urls import path
from . import views

urlpatterns = [
    path('cash_machine/', views.load_bill),
]

