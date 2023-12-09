from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request,"User/Profile.html")
def booking(request):
    return render(request,"User/Booking.html")