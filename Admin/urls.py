from django.urls import path,include
from Admin import views
app_name = 'webadmin'
urlpatterns = [
    path('district/',views.district,name="district"),
    path('deldistrict/<str:id>',views.deldistrict,name="deldistrict"),
    path('updatedistrict/<str:id>',views.updatedistrict,name="updatedistrict"),
    path('branch/',views.branch,name="branch"),
    path('place/',views.place,name="place"),
    path('delplace/<str:id>',views.delplace,name="delplace"),
    path('updateplace/<str:id>',views.updateplace,name="updateplace"),
    path('category/',views.category,name="category"),
    path('delcategory/<str:id>',views.delcategory,name="delcategory"),
    path('updatecategory/<str:id>',views.updatecategory,name="updatecategory"),
    path('subcategory/',views.subcategory,name="subcategory"),
    path('delsubcategory/<str:id>',views.delsubcategory,name="delsubcategory"),
    path('updatesubcategory/<str:id>',views.updatesubcategory,name="updatesubcategory"),
]