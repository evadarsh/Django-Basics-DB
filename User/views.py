from django.shortcuts import render
import firebase_admin
from firebase_admin import storage,auth,credentials,firestore
import pyrebase

db = firestore.client()
# Create your views here.
def profile(request):
    return render(request,"User/Profile.html")
def booking(request):
    return render(request,"User/Booking.html")

def userreg(request):
    dis = db.collection("tbl_district").stream()
    dis_data = []
    for d in dis:
        dis_data.append({"district":d.to_dict(),"id":d.id})
    return render(request,"User/Registration.html",{"district":dis_data})

def ajaxplace(request):
    place = db.collection("tbl_place").where("district_id", "==", request.GET.get("disd")).stream()
    place_data = []
    for p in place:
        place_data.append({"place":p.to_dict(),"id":p.id})
    return render(request,"User/AjaxPlace.html",{"place":place_data})