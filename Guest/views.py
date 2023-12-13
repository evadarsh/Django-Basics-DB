from django.shortcuts import render
import firebase_admin
from firebase_admin import storage,auth,credentials,firestore
import pyrebase

db = firestore.client()
# Create your views here.
def registration(request):
    cat = db.collection("tbl_category").stream()
    cat_data = []
    for i in cat:
        data = i.to_dict()
        cat_data.append({"category":data,"id":i.id})
    
    dis = db.collection("tbl_district").stream()
    dis_data = []
    for d in dis:
        dis_data.append({"district":d.to_dict(),"id":d.id})
    return render(request,"Guest/Registration.html",{"district":dis_data,"category":cat_data})

def ajaxplace(request):
    place = db.collection("tbl_place").where("district_id", "==", request.GET.get("disd")).stream()
    place_data = []
    for p in place:
        place_data.append({"place":p.to_dict(),"id":p.id})
    return render(request,"Guest/AjaxPlace.html",{"place":place_data})

def ajaxsubcategory(request):
    subcategory = db.collection("tbl_subcategory").where("category_id", "==", request.GET.get("catd")).stream()
    subcategory_data = []
    for s in subcategory:
        subcategory_data.append({"subcategory":s.to_dict(),"id":s.id})
    return render(request,"Guest/AjaxSubcategory.html",{"subcategory":subcategory_data})