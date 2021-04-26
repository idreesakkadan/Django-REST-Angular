from django.urls import path
from .views import *

urlpatterns = [

    path('',StudentCreateView.as_view(),name='studentaddpage'),
    path('update/<int:pk>',StudentEditView.as_view(),name='updatepage'),
    
]