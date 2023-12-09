from django.urls import path,include
from User import views
urlpatterns = [
     path('profile/',views.profile),
     path('booking/',views.booking),
]