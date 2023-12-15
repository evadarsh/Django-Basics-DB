from django.shortcuts import render,redirect
import firebase_admin
from firebase_admin import storage,auth,credentials,firestore
import pyrebase
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages

db = firestore.client()
# Create your views here.

def home(request):
    user = db.collection("tbl_user").document(request.session["uid"]).get().to_dict()
    return render(request,"User/HomePage.html",{"user":user})

def profile(request):
    if 'uid' in request.session:
        user = db.collection("tbl_user").document(request.session["uid"]).get().to_dict()
        return render(request,"User/Profile.html",{'user':user})
    else:
        return redirect("webguest:login")

def editprofile(request):
    if 'uid' in request.session:
        data = db.collection("tbl_user").document(request.session["uid"]).get().to_dict()
        if request.method == "POST":
            data = {'user_name':request.POST.get('txt_name'),'user_contact':request.POST.get('txt_contact'),'user_address':request.POST.get('txt_address')}
            db.collection("tbl_user").document(request.session["uid"]).update(data)
            return redirect("webuser:profile")
        else:
            return render(request,"User/EditProfile.html",{'user':data})
    else:
        return redirect("webguest:login")

def changepassword(request):
    user = db.collection("tbl_user").document(request.session["uid"]).get().to_dict()
    email = user["user_email"]
    pass_link = firebase_admin.auth.generate_password_reset_link(email)
    send_mail(
        'Reset your password ', #subject
        "\rHello \r\nFollow this link to reset your Project password for your " + email + "\n" + pass_link +".\n If you didn't ask to reset your password, you can ignore this email. \r\n Thanks. \r\n Your D MARKET team.",#body
        settings.EMAIL_HOST_USER,
        [email],
    )
    return render(request,"User/Profile.html",{"msg":email})


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