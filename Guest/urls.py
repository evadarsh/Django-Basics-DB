from django.urls import path,include
from Guest import views
app_name = "webguest"
urlpatterns = [
     path('registration/',views.registration),
     path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
     path('ajaxsubcategory/',views.ajaxsubcategory,name="ajaxsubcategory"),
]