from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import storage,auth,credentials,firestore
import pyrebase
# Create your views here.

cred = credentials.Certificate("DB\mainproject-122fe-firebase-adminsdk-odmtf-8b97e8e17a.json")
app = firebase_admin.initialize_app(cred)

db = firestore.client()

def district(request):
    if request.method == "POST":
        data = {"district_name":request.POST.get("txt_district")}
        db.collection("tbl_district").add(data)
        return redirect("webadmin:district")
    else:
        return render(request,"Admin/District.html")
    
def branch(request):
    if request.method == "POST":
        data = {"branch_name":request.POST.get("txt_branch")}
        db.collection("tbl_branch").add(data)
        return redirect("webadmin:branch")
    else:
        return render(request,"Admin/Branch.html")