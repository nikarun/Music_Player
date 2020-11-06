from django.shortcuts import render,redirect
from django.http import HttpResponse as hr
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate,logout

def album(request):
    check=request.user.is_authenticated
    data = Album.objects.all().order_by("name")
    dict={"album":data,"check":check}
    return render(request,"album.html",dict)
def album_details(request,a_id):
        data=Album.objects.get(id = a_id)
        dat=Song.objects.filter(album_id=data)
        dict={"album":data,"song":dat}
        return render(request,"album_details.html",dict)

def song_list(request):
    data=Song.objects.all()
    dict={"song":data}
    return render(request,"songlist.html",dict)

def add_album(request):
    if not request.user.is_authenticated:
        return redirect("Login")
    if request.method=="POST":
        dict=request.POST
        album_name=dict["album_name"]
        album_artist = dict["album_artist"]
        album_banner = request.FILES["album_banner"]
        print(album_name,album_artist,album_banner)
        Obj=Album()
        Obj.name=album_name
        Obj.artist=album_artist
        Obj.image=album_banner
        Obj.save()
        return redirect('album')
    return render(request,"add_album.html")

def add_song(request):
    if not request.user.is_authenticated:
        return redirect("Login")
    data=Album.objects.all()
    dict={"data":data}
    if request.method=="POST":
        Dict=request.POST
        name=Dict["song_title"]
        album_id=Dict["album"]
        song=request.FILES["song_file"]
        album=Album.objects.get(id=album_id)
        Obj=Song()
        Obj.title=name
        Obj.album_id=album
        Obj.file=song
        Obj.save()
        return redirect("album_details",album_id)
    return render(request,"add_song.html",dict)

def Login(request):
    last_user=""
    error=None
    print(request.method)
    if request.method == "POST":
        Dict=request.POST
        print(Dict)
        name = Dict["username"]
        last_user=name
        password = Dict["password"]
        user=authenticate(username=name,password=password)
        if user != None:
            login(request,user)
            return redirect("album")
        else:
            error="Wrong Username And Password"
    return render(request,"login.html",{"error":error,"last_user":last_user})

def Logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("album")
    return hr("logged out")

def Register(request):
    error=None
    user=None
    if request.method=="POST":
        data=request.POST
        name=data["name"]
        un=data["user_name"]
        email=data["email"]
        password=data["password1"]
        pass2=data["password2"]
        if(password != pass2):
            error="Passwords do not match"
            return render(request,"register.html",{"error":error})
        try:
            user = User.objects.get(username=un)
            error = "username already exist"
        except:
            usr = User.objects.create_user(un, email, password)
            usr.first_name = name
            usr.save()
            return redirect("Login")

    return render(request,"register.html",{"error":error})

def Delete(request,a_id):
    if request.user.is_authenticated:
        data=Album.objects.get(id=a_id)
        data.delete()
        return redirect("album")
    else:
        return redirect("Login")