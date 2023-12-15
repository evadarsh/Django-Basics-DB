from django.urls import path,include
from User import views
app_name = "webuser"
urlpatterns = [
     path('home/',views.home,name="home"),
     path('profile/',views.profile,name="profile"),
     path('editprofile/',views.editprofile,name="editprofile"),
     path('changepassword/',views.changepassword,name="changepassword"),
     path('booking/',views.booking),
     path('userreg/',views.userreg,name="userreg"),
     path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
]