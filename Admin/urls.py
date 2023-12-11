from django.urls import path,include
from Admin import views
app_name = 'webadmin'
urlpatterns = [
    path('district/',views.district,name="district"),
    path('branch/',views.branch,name="branch"),
    path('place/',views.place,name="place"),
    path('category/',views.category,name="category"),
    path('subcategory/',views.subcategory,name="subcategory"),
]