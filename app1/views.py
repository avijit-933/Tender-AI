from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Officer
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import Tender

from .forms import TenderForm


from .models import Tender





from .forms import TenderForm
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
    
    

@login_required
def createtender(request):
    username = request.user.officer.name 
    return render(request, 'createtender.html',{'username': username})

@login_required
def evaluation(request):
     username = request.user.officer.name
     return render(request, 'evaluation.html',{'username': username})

@login_required
def managetender(request):
    username = request.user.officer.name
    return render(request, 'managetender.html',{'username': username})







def managetender(request):
    # Fetch only the required fields from Tender
    tenders = Tender.objects.values('tender_id', 'title', 'department', 'last_date')
    
    # Pass as context to template
    context = {
        'tenders': tenders,
        'username': request.user.username if request.user.is_authenticated else None
    }
    return render(request, 'managetender.html', context)

@login_required
def createtender(request):
    draft_message = None

    if request.method == "POST":
        form = TenderForm(request.POST, request.FILES)
        if form.is_valid():
            tender = form.save(commit=False)
            tender.created_by = request.user

            # Determine if draft or publish
            if 'draft' in request.POST:
                tender.status = 'draft'
                draft_message = "Tender saved as draft successfully!"
            elif 'publish' in request.POST:
                tender.status = 'published'
            tender.save()
            if draft_message:
                # reload page to show draft message
                form = TenderForm()  # empty form
        else:
            messages.error(request, "Please fix errors below.")
    else:
        form = TenderForm()

    context = {
        'form': form,
        'draft_message': draft_message,
        'username': request.user.username,
    }
    return render(request, 'createtender.html', context)

def browse_tenders(request):
    return render(request, "browse_tenders.html")
def submit_bid(request):
    return render(request, "submit_bid.html")
def track_submissions(request):
    return render(request, "track_submissions.html")
def watchedtenders(request):
    return render(request, "watchtenders.html")
