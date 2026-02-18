from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Officer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'index.html')



# ================= REGISTER VIEW =================
def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
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


# ================= LOGIN VIEW =================
def officer_login(request):
    if request.method == "POST":
        email = request.POST.get("email")
        emp_id = request.POST.get("emp_id")
        password = request.POST.get("password")
        remember = request.POST.get("remember_me")

        try:
            officer = Officer.objects.get(email=email, emp_id=emp_id)
        except Officer.DoesNotExist:
            messages.error(request, "Invalid Email or Employee ID")
            return render(request, "login.html")

        # Authenticate using email as username
        user = authenticate(request, username=email, password=password)

        if user is not None:
            login(request, user)

            # Remember Me
            if not remember:
                request.session.set_expiry(0)

            return redirect("Government_dashboard")
        else:
            messages.error(request, "Invalid Password")

    return render(request, "login.html")



def forget(request):
    return render(request, 'forget.html')


@login_required
def dashboard(request):
    return render(request, 'Government_dashboard.html')


def Companydashboard(request):
    # Add some context data if needed
    
    return render(request, 'bidder/Companydashboard.html')

def browse_tenders(request):
    return render(request, 'bidder/browse_tenders.html') 
def submit_bid(request):
    return render(request, 'bidder/submit_bid.html') 
def submission_status(request):
    return render(request, 'bidder/submission_status.html') 
def watch_tenders(request):
    return render(request, 'bidder/watch_tenders.html') 
def logout(request):
     return redirect('home') 
# def evaluationdashboard(request):
#     return render(request,'evaluator/evaluationdashboard.html')


