from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import storage,auth,credentials,firestore
import pyrebase

config = {
  "apiKey": "AIzaSyACpb3W02pzE0Q_lnJsC7LoiDvEVU0znPU",
  "authDomain": "mainproject-122fe.firebaseapp.com",
  "projectId": "mainproject-122fe",
  "storageBucket": "mainproject-122fe.appspot.com",
  "messagingSenderId": "797132027159",
  "appId": "1:797132027159:web:551dd5a1eebcd9089cb352",
  "measurementId": "G-7C4G2DT8T2",
  "databaseURL":""
}
firebase = pyrebase.initialize_app(config)
authe = firebase.auth()
sd = firebase.storage()

db = firestore.client()

def registration(request):
    dis = db.collection("tbl_district").stream()
    dis_data = []
    for i in dis:
        data = i.to_dict()
        dis_data.append({"district":data,"id":i.id})
    
    cat = db.collection("tbl_category").stream()
    cat_data = []
    for i in cat:
        data = i.to_dict()
        cat_data.append({"category":data,"id":i.id})
    
    if request.method == "POST":
        email = request.POST.get("txt_email")
        password = request.POST.get("txt_password")
        try:
            user = firebase_admin.auth.create_user(email=email,password=password)
        except (firebase_admin._auth_utils.EmailAlreadyExistsError,ValueError) as error:
            return render(request,"Guest/Registration.html",{"msg":error})

        image = request.FILES.get("txt_photo")
        if image:
            path = "Example/" + image.name
            sd.child(path).put(image)
            download_url = sd.child(path).get_url(None)
        
        user = {"user_id":(user.uid),
                "user_name":request.POST.get("txt_name"),
                "user_contact":request.POST.get("txt_contact"),
                "user_email":request.POST.get("txt_email"),
                "user_address":request.POST.get("txt_address"),
                "user_place":request.POST.get("sel_place"),
                "user_subcategory":request.POST.get("sel_place"),
                "user_photo":(download_url),}
        db.collection("tbl_user").add(user)
        return redirect("webguest:registration")
    else:
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

def login(request):
    userid=""
    adminid=""
    if request.method =="POST":
        email = request.POST.get("txt_email")
        password = request.POST.get("txt_password")

        try:
            data = authe.sign_in_with_email_and_password(email,password)
        except:
            return render(request,"Guest/Login.html",{"msg":"INVALID_LOGIN_CREDENTIALS... Check Email and Password"})
        id = data["localId"]
        user_data = db.collection("tbl_user").where("user_id", "==", id).stream()
        for u in user_data:
            userid = u.id
        admin_data = db.collection("tbl_admin").where("admin_id", "==", id).stream()
        for a in admin_data:
            adminid = a.id
        if userid:
            request.session["uid"] = userid
            return redirect("webuser:home")
        elif adminid:
            request.session["aid"] = adminid
            return redirect("webadmin:home")
        else:
            return render(request,"Guest/Login.html",{"msg":"Error in Login"})
    else:
        return render(request,"Guest/Login.html")


# def fileupload(request):
#     if request.method == "POST":
#         image = request.FILES.get("txt_photo")
#         if image:
#             path = "Example/" + image.name
#             sd.child(path).put(image)
#             download_url = sd.child(path).get_url(None)
#         print(download_url)
#         return render(request,"Guest/FileUpload.html")
#     else:
#         return render(request,"Guest/FileUpload.html")