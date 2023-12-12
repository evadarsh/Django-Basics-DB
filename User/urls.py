from django.urls import path,include
from User import views
app_name = "webuser"
urlpatterns = [
     path('profile/',views.profile),
     path('booking/',views.booking),
     path('userreg/',views.userreg,name="userreg"),
     path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
]