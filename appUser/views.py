from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User 
from django.contrib import messages
from .models import *
# Create your views here.


def Browse(request):
    profils = Profile.objects.filter(user=request.user)
    
    # kullanıcıya ait profillerin sayısını bul, bulunan sayıyı koşul ile bağla, en fazla 4 profil olucak

    if request.method == "POST":
        button = request.POST.get("button")
        
        if button == "login-profil":
            password = request.POST.get("profil-password")
            profilid = request.POST.get("profilid")

            profil = Profile.objects.get(id=profilid)
            
            if password == profil.password:
                return redirect('/indexBrowse/{}/'.format(profil.slug))
            else:
                messages.warning(request,'Şifreniz Hatalı')
            
        else:
            name = request.POST.get("profile-name")
            image = request.FILES.get("image")
            password = request.POST.get("password")
            active = request.POST.get("active")
            
            if name:
                if active == None:
                    active = False
                
                if button == "create":
                    if len(profils) < 4:
                        profile = Profile(user=request.user ,name=name, image=image, password=password, password_active=active)
                        profile.save()
                        
                if button == "update":
                    profilid = request.POST.get("profil-id")
                    profil = Profile.objects.get(id=profilid)
                    profil.name = name
                    if image != None:
                        profil.image = image
                    profil.password = password
                    profil.password_active = active
                    profil.save()
        
                
        return redirect("Browse")
    
    context={
        "profils": profils,
    }
    return render(request, 'user/browse.html', context)


def profileDelete(request,profilid):
    profil = Profile.objects.get(id=profilid)
    profil.delete()
    return redirect("Browse")


def Account(request):
    context={}
    return render(request, 'user/hesap.html', context)


def loginUser(request):
    
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        if "@" in username:
            if User.objects.filter(email=username).exists():
                # kullanıcılar arasında emaili eşleşeni bul ve o kullanıcının username'i çek
                username = User.objects.filter(email=username).get().username
            else:
                messages.error(request, 'Bu email yada şifre yanlış')
            
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request,user)
            return redirect('Browse')
        else:
            messages.error(request, 'Bu kullanıcı adı yada şifre yanlış')
    
    context={}
    return render(request, 'user/login.html', context)


def registerUser(request):
    
    if request.method == "POST":
        name = request.POST.get("name")
        surname = request.POST.get("surname")
        email = request.POST.get("email")
        tel = request.POST.get("tel")
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        
        # password kontrol, username, email, 
        
        if password1==password2:
            if tel.isnumeric():
                if not User.objects.filter(username=username).exists():
                    if not User.objects.filter(email=email).exists():
                        user = User.objects.create_user(first_name=name, last_name=surname, username=username, password=password1, email=email)
                        user.save()
                        
                        userinfo = Userinfo(user=user,password=password1, tel=tel)
                        userinfo.save()
                        
                        profile = Profile(user=user, name=name)
                        profile.save()
                        
                        return redirect("loginUser")
                    else:
                        messages.error(request, 'bu email zaten kullanılıyor!')
                else:
                    messages.error(request, 'bu kullanıcı adı zaten kullanılıyor!')
            else:
                messages.error(request, 'Telefon numarasını düzgün giriniz!')
        else:
            messages.error(request, 'şifreler aynı değil!')
                    
                    
    
    context={}
    return render(request,'user/register.html', context)




def logoutUser(request):
    logout(request)
    return redirect('index')