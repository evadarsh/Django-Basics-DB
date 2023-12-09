from django.urls import path,include
from Admin import views
app_name = 'webadmin'
urlpatterns = [
    path('district/',views.district,name="district"),
]