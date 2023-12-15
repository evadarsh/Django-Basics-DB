from django.urls import path,include
from Guest import views
app_name = "webguest"
urlpatterns = [
     path('registration/',views.registration,name="registration"),
     path('ajaxplace/',views.ajaxplace,name="ajaxplace"),
     path('ajaxsubcategory/',views.ajaxsubcategory,name="ajaxsubcategory"),
     path('login/',views.login,name="login"),
     # path('fileupload/',views.fileupload,name="fileupload"),
]