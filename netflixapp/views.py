from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .models import Video, Card
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

def LoginPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        username = User.objects.get(email=email)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request,"Username or Password is incorrect....")
            
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')

def SignUpFirst(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email=="":
            return redirect('in')
    return render(request, 'signupfirst.html')

def SignUpSecond(request):
   return render(request, 'signupsecond.html')

def SignUpThird(request):
    if request.method=="POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email=="":
            return redirect('signupsecond')
        else:
            username = ""
            for i in email:
                if i=='@':
                    break
                else:
                    username = username + i
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        login(request, user)
    return render(request, 'signupthird.html')

def SignUpFourth(request):
    return render(request, 'signupfourth.html')

def SignUpFifth(request):
    if request.method=="POST":
        plan = request.POST.get('plan')
        request.session['plan']=plan
        print(plan)
    return render(request, 'signupfifth.html')

def SignUpSixth(request):
    plan = request.session.get('plan')
    context = {'plan':plan}
    return render(request, 'signupsixth.html', context)

def Dashboard(request):
    searched = None
    if request.method=='POST':
        if request.POST.get('searchquery')=='searchquery':
            search = request.POST.get('search')
            if search !="":
                searched = Video.objects.filter(name__icontains=search)
                print(searched)
            elif search=="":
                searched = None
                print(searched)
        else:
            name = request.POST.get('name')
            cardnumber = request.POST.get('cardnumber')
            expirydate = request.POST.get('expirydate')
            securitycode = request.POST.get('securitycode')
            user = request.user
            if expirydate=="":
                return redirect('signupsixth')
            else:
                card = Card.objects.create(user=user, name=name, cardnumber=cardnumber, expirydate=expirydate, securitycode=securitycode)
                card.save()
    user = request.user
    tvseries = Video.objects.filter(category=1)
    movies = Video.objects.filter(category=2)
    context = {'tvseries':tvseries, 'movies':movies, 'user':user, 'searched':searched}
    return render(request, 'dashboard.html', context)

def Movie(request,id):
    video = Video.objects.get(id=id)
    context = {'video':video}
    return render(request, 'moviedetail.html', context)

def TVSeries(request):
    tvseries = Video.objects.filter(category=1)
    context = {'tvseries':tvseries}
    return render(request, 'tvseries.html', context)

def Movies(request):
    movies = Video.objects.filter(category=2)
    context = {'movies':movies}
    return render(request, 'movies.html', context)