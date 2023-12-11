from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import storage,auth,credentials,firestore
import pyrebase
# Create your views here.

cred = credentials.Certificate("DB\mainproject-122fe-firebase-adminsdk-odmtf-8b97e8e17a.json")
app = firebase_admin.initialize_app(cred)

db = firestore.client()

def district(request):
    dis = db.collection("tbl_district").stream()
    dis_data = []
    for i in dis:
        data = i.to_dict()
        dis_data.append({"district":data,"id":i.id})
    # print(dis_data)
    if request.method == "POST":
        data = {"district_name":request.POST.get("txt_district")}
        db.collection("tbl_district").add(data)
        return redirect("webadmin:district")
    else:
        return render(request,"Admin/District.html",{"dis":dis_data})
    
def place(request):
    plc = db.collection("tbl_place").stream()
    plc_data = []
    for i in plc:
        data = i.to_dict()
        plc_data.append({"place":data,"id":i.id})
    if request.method == "POST":
        data = {"place_name":request.POST.get("txt_place")}
        db.collection("tbl_place").add(data)
        return redirect("webadmin:place")
    else:
        return render(request,"Admin/Place.html",{"plc":plc_data})
    
def branch(request):
    brn = db.collection("tbl_branch").stream()
    brn_data = []
    for i in brn:
        data = i.to_dict()
        brn_data.append({"branch":data,"id":i.id})
    if request.method == "POST":
        data = {"branch_name":request.POST.get("txt_branch")}
        db.collection("tbl_branch").add(data)
        return redirect("webadmin:branch")
    else:
        return render(request,"Admin/Branch.html",{"brn":brn_data})
def category(request):
    cat = db.collection("tbl_category").stream()
    cat_data = []
    for i in cat:
        data = i.to_dict()
        cat_data.append({"category":data,"id":i.id})
    if request.method == "POST":
        data = {"category_name":request.POST.get("txt_category")}
        db.collection("tbl_category").add(data)
        return redirect("webadmin:category")
    else:
        return render(request,"Admin/Category.html",{"cat":cat_data})
def subcategory(request):
    subcat = db.collection("tbl_category").stream()
    subcat_data = []
    for i in subcat:
        data = i.to_dict()
        subcat_data.append({"subcat":data,"id":i.id})
    if request.method == "POST":
        data = {"subcategory_name":request.POST.get("txt_subcategory"),"category_id":request.POST.get("sel_category")}
        db.collection("tbl_subcategory").add(data)
        return redirect("webadmin:subcategory")
    else:
        return render(request,"Admin/SubCategory.html",{"subcat":subcat_data})