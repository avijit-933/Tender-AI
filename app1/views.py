from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Officer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth import logout as auth_logout 
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Bidder

def home(request):
    return render(request, 'index.html')



# ================= REGISTER VIEW =================
def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        request.session['username'] = name
        email = request.POST.get("email")
        emp_id = request.POST.get("emp_id")
        phone = request.POST.get("phone")
        password = request.POST.get("password")

        # Check duplicate email
        if Officer.objects.filter(email=email).exists():
            messages.error(request, "Email already registered")
            return render(request, "register.html")

        # Check duplicate emp id
        if Officer.objects.filter(emp_id=emp_id).exists():
            messages.error(request, "Employee ID already exists")
            return render(request, "register.html")

        # Create Django User (IMPORTANT)
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        # Create Officer profile
        Officer.objects.create(
            user=user,
            name=name,
            email=email,
            emp_id=emp_id,
            phone=phone
        )

        messages.success(request, "Registration successful. Please login.")
        return redirect("login")

    return render(request, "register.html")

def bidder_register(request):
    if request.method == "POST":
        company_name = request.POST.get('companyName')
        registration_number = request.POST.get('registrationNumber')
        gst = request.POST.get('gst')
        pan = request.POST.get('pan')
        address = request.POST.get('address')

        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        # Check if email already exists
        if User.objects.filter(username=email).exists():
            messages.error(request, "Email already registered")
            return redirect('bidder_register')

        # Create user
        user = User.objects.create_user(
            username=email,
            email=email,
            password=password
        )

        # Create bidder profile
        Bidder.objects.create(
            user=user,
            company_name=company_name,
            registration_number=registration_number,
            gst_number=gst,
            pan_number=pan,
            address=address,
            phone=phone,
        )

        messages.success(request, "Registration successful. Please login.")
        return redirect('login_view')

    return render(request, 'company_register.html')


# ================= LOGIN VIEW =================
def officer_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        emp_id = request.POST.get("emp_id")
        password = request.POST.get("password")

        try:
            officer = Officer.objects.get(email=email, emp_id=emp_id)
        except Officer.DoesNotExist:
            messages.error(request, "Invalid Email or Employee ID")
            return render(request, "login.html")

        # Get linked Django user
        user = officer.user

        # Authenticate using linked username
        user = authenticate(request, username=user.username, password=password)

        if user is not None:
            login(request, user)
            return redirect("Government_dashboard")
            
        else:
            messages.error(request, "Invalid Password")

    return render(request, "login.html")


def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Authenticate using username=email
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect('company_dashboard')
        else:
            messages.error(request, "Invalid Gmail or password")

    return render(request, 'company_login.html')




def forget(request):
    return render(request, 'forget.html')


@login_required
def dashboard(request):
    username = request.user.officer.name 
     
    return render(request, 'Government_dashboard.html', {'username': username})
    
    

def createtender(request):
    return render(request, 'createtender.html')
def evaluation(request):
    return render(request, 'evaluation.html')
def managetender(request):
    return render(request, 'managetender.html')


