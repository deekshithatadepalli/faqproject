# faq/urls.py
from django.urls import path
from .views import faq_list

urlpatterns = [
    path('faqs/', faq_list, name='faq-list'),  # Ensure this is the correct route
]
