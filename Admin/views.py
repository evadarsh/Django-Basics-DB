from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import storage,auth,credentials,firestore
import pyrebase
# Create your views here.

db = firestore.client()

def district(request):
    dis = db.collection("tbl_district").stream()
    dis_data = []
    for i in dis:
        data = i.to_dict()
        dis_data.append({"district":data,"id":i.id})
    if request.method == "POST":
        data = {"district_name":request.POST.get("txt_district")}
        db.collection("tbl_district").add(data)
        return redirect("webadmin:district")
    else:
        return render(request,"Admin/District.html",{"dis":dis_data})
    
def deldistrict(request,id):
    db.collection("tbl_district").document(id).delete()
    return redirect("webadmin:district")

def updatedistrict(request,id):
    dis = db.collection("tbl_district").document(id).get().to_dict()
    if request.method == "POST":
        data = {"district_name":request.POST.get("txt_district")}
        db.collection("tbl_district").document(id).update(data)
        return redirect("webadmin:district")
    else:
        return render(request,"Admin/District.html",{"district":dis})
    
def place(request):
    district = db.collection("tbl_district").stream()
    district_data = []
    for dis in district:
        district_data.append({"district":dis.to_dict(),"id":dis.id})
    plc = db.collection("tbl_place").stream()
    plc_data = []
    for s in plc:
        pdata = s.to_dict()
        dis_data = db.collection("tbl_district").document(pdata["district_id"]).get().to_dict()
        plc_data.append({"district":dis_data,"place":pdata,"id":s.id})
    if request.method == "POST":
        data = {"place_name":request.POST.get("txt_place"),"district_id":request.POST.get("sel_district")}
        db.collection("tbl_place").add(data)
        return redirect("webadmin:place")
    else:
        return render(request,"Admin/Place.html",{"dis":district_data,"plc":plc_data})

def delplace(request,id):
    db.collection("tbl_place").document(id).delete()
    return redirect("webadmin:place")

def updateplace(request,id):
    district = db.collection("tbl_district").stream()
    dist_data = []
    for c in district:
        dist_data.append({"district":c.to_dict(),"id":c.id})
    plc = db.collection("tbl_place").document(id).get().to_dict()
    if request.method == "POST":
        data = {"place_name":request.POST.get("txt_place"),"district_id":request.POST.get("sel_district")}
        db.collection("tbl_place").document(id).update(data)
        return redirect("webadmin:place")
    else:
        return render(request,"Admin/Place.html",{"place":plc,"dis":dist_data})
    
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

def delcategory(request,id):
    db.collection("tbl_category").document(id).delete()
    return redirect("webadmin:category")

def updatecategory(request,id):
    cat = db.collection("tbl_category").document(id).get().to_dict()
    if request.method == "POST":
        data = {"category_name":request.POST.get("txt_catagory")}
        db.collection("tbl_category").document(id).update(data)
        return redirect("webadmin:category")
    else:
        return render(request,"Admin/Category.html",{"category":cat})

def subcategory(request):
    category = db.collection("tbl_category").stream()
    category_data = []
    for cat in category:
        category_data.append({"category":cat.to_dict(),"id":cat.id})

    subcat = db.collection("tbl_subcategory").stream()
    subcat_data = []
    for s in subcat:
        sdata = s.to_dict()
        cat_data = db.collection("tbl_category").document(sdata["category_id"]).get().to_dict()
        subcat_data.append({"Category":cat_data,"subcategory":sdata,"id":s.id})
    if request.method == "POST":
        data = {"subcategory_name":request.POST.get("txt_subcategory"),"category_id":request.POST.get("sel_category")}
        db.collection("tbl_subcategory").add(data)
        return redirect("webadmin:subcategory")
    else:
        return render(request,"Admin/SubCategory.html",{"cat":category_data,"subcat":subcat_data})
    
def delsubcategory(request,id):
    db.collection("tbl_subcategory").document(id).delete()
    return redirect("webadmin:subcategory")

def updatesubcategory(request,id):
    category = db.collection("tbl_category").stream()
    cate_data = []
    for c in category:
        cate_data.append({"category":c.to_dict(),"id":c.id})

    subcat = db.collection("tbl_subcategory").document(id).get().to_dict()
    if request.method == "POST":
        data = {"subcategory_name":request.POST.get("txt_subcategory"),"category_id":request.POST.get("sel_category")}
        db.collection("tbl_subcategory").document(id).update(data)
        return redirect("webadmin:subcategory")
    else:
        return render(request,"Admin/SubCategory.html",{"subcategory":subcat,"cat":cate_data})