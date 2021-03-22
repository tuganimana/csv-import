from django.urls import path
from .views import *
from .import views
urlpatterns = [
    path('uploadcsv/', Uploadcsvs.as_view(),name=''),
   
]