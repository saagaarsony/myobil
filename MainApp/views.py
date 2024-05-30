from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from rest_framework import generics
from .models import Per_Details, Bus_Details
from .serializers import LogSerializer, BusinessSerializer

# Start The Logical And Pageing Code.

# That Is For API
class LogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Per_Details.objects.all()
    serializer_class = LogSerializer

class LogRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Per_Details.objects.all()
    serializer_class = LogSerializer

class BusinessListCreateAPIView(generics.ListCreateAPIView):
    queryset = Bus_Details.objects.all()
    serializer_class = BusinessSerializer

class BusinessRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bus_Details.objects.all()
    serializer_class = BusinessSerializer
    
# That IS For Home Page.
def home(request):
    return render(request, 'home.html')

# That Is For Personal Registration Page
def per_reg(request):
    error = "" 
    if request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        profile = request.FILES.get('profile')
        #logo = request.FILES.get('logo')
    
        try:
            user = User.objects.create_user(username=mobile, password=pwd)  
            log_details = Per_Details.objects.create(user=user, name=name, lastname=lastname, email=email, mobile=mobile, profile=profile)
            log_details.save()
            error = "no"  
        except Exception as e:
            error = "yes"  
            print(e)  

    return render(request, '00Registration/001_per_reg.html', {'error': error})

# That Is For Business Registration
def Business_reg(request):
    error = ""
    if request.method == "POST":
        name = request.POST.get('name')
        lastname = request.POST.get('lastname')
        pwd = request.POST.get('pwd')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        #profile = request.FILES.get('profile')
        logo = request.FILES.get('logo')
        
        try:
            user = User.objects.create_user(username=mobile, password=pwd)  
            log_Business = Bus_Details.objects.create(user=user, name=name, lastname=lastname, email=email, mobile=mobile, logo=logo)
            log_Business.save()
            error = "no"  
        except Exception as e:
            error = "yes"  
            print(e)  

    return render(request, '00Registration/003_business_reg.html', {'error': error})  

# That Is For Login Page (persnal)
def login_view(request):
    error = ""  

    def is_personal_user(user):        
        return Per_Details.objects.filter(user=user).exists()
    if request.method == 'POST':
        u = request.POST['umobile']
        p = request.POST['password']
        user = authenticate(username=u, password=p)
        if user is not None:
            auth_login(request, user)  
            if is_personal_user(user):
                return redirect('Per_home')  
            else:
                return redirect('business_home')  
        else:
            error = "yes"
    return render(request, '00Registration/002_login.html', {'error': error})

# That Is For change password
@login_required
def change_pass(request):
    if not request.user.is_authenticated:
        return redirect('login')
    error = ""
    user = request.user
    if request.method == "POST":
        cp = request.POST['currentpass']
        np = request.POST['newpass']
        try :
            if user.check_password(cp):
                user.set_password(np)
                user.save()
                error = "no"
            else :
                error = "not"    
        except:
           error = "yes"
    return render(request,'password/changepass.html', locals())   

# That Is For Personal Home Page
@login_required
def Per_home(request):
    try:
        private_details = Per_Details.objects.get(user=request.user)
    except Per_Details.DoesNotExist:
        private_details = None
    context = {
        'bus_details': private_details
    }
    return render(request, 'home/Personal_home.html' , {'private_details': private_details})

# That Is For Update The Page Personal User
@login_required
def per_profile(request):
    user = request.user
    try:
        log_details = Per_Details.objects.get(user=user)
    except Per_Details.DoesNotExist:
        log_details = Per_Details.objects.create(user=user)

    if request.method == "POST":
       
        log_details.name = request.POST.get('name')
        log_details.lastname = request.POST.get('lastname')
        log_details.email = request.POST.get('email')
        log_details.mobile = request.POST.get('mobile')
        #FUll Profile
        log_details.city = request.POST.get('city')
        log_details.pin = request.POST.get('pin')
        log_details.contry = request.POST.get('contry')
        log_details.email = request.POST.get('email')
        log_details.wmobile = request.POST.get('wmobile')
        log_details.gender = request.POST.get('gender')
        log_details.married = request.POST.get('married')
        log_details.occupation = request.POST.get('occupation')
        
        if 'profile' in request.FILES:
            log_details.profile = request.FILES['profile']
        
        log_details.save()
        return redirect('Per_home')  
    return render(request, 'updateprofile/personal_update.html', {'log_details': log_details})

# That Is For Business Home Page
@login_required
def business_home(request):
    try:
        bus_details = Bus_Details.objects.get(user=request.user)
    except Bus_Details.DoesNotExist:
        bus_details = None
    context = {
        'bus_details': bus_details
    }
    return render(request, 'home/business_home.html' , {'bus_details': bus_details})

# That Is For Business Profile Update
@login_required
def update_businessprofile(request):
    user = request.user
    try:
        log_business = Bus_Details.objects.get(user=user)
    except Bus_Details.DoesNotExist:
        log_business = Bus_Details.objects.create(user=user)

    if request.method == "POST":
        
        log_business.name = request.POST.get('name')
        log_business.lastname = request.POST.get('lastname')
        log_business.email = request.POST.get('email')
        log_business.mobile = request.POST.get('mobile')
        log_business.gst = request.POST.get('gst')
        log_business.tag = request.POST.get('tag')
        log_business.dis = request.POST.get('dis')
        log_business.category = request.POST.get('category')
        log_business.add = request.POST.get('add')
        log_business.city = request.POST.get('city')
        log_business.country = request.POST.get('country')
        log_business.pin = request.POST.get('pin')

        
        if 'logo' in request.FILES:
            log_business.logo = request.FILES['logo']

        
        log_business.save()

        return redirect('business_home')  
    return render(request, 'updateprofile/business_update.html', {'log_business': log_business})

# That Is For LogOut The User
def Loogout(request):
    logout(request)
    return redirect('home')