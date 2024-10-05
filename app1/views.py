from django.shortcuts import render, redirect
from .models import Doctor, Appointment
from django.contrib.auth import login,logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import PatientRegistrationForm
from django.utils import timezone

# View to list all doctors
def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'POST':
        form = PatientRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user after registration
            return redirect('home')  # Redirect to home page or wherever
    else:
        form = PatientRegistrationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Redirect to the homepage after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'doctor_list.html', {'doctors': doctors})

# View for booking appointments
@login_required
def book_appointment(request, doctor_id):
    doctor = Doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        appointment = Appointment.objects.create(
            patient=request.user,
            doctor=doctor,
            appointment_date=timezone.now(),
            status='Booked'
        )
        return redirect('appointment_history')
    return render(request, 'book_appointment.html', {'doctor': doctor})

# View for patient to see their appointment history
@login_required
def appointment_history(request):
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'appointment_history.html', {'appointments': appointments})

def appointment_history(request):
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'appointment_history.html', {'appointments': appointments})

def patient_dashboard(request):
    appointments = Appointment.objects.filter(patient=request.user)
    return render(request, 'patient_dashboard.html', {'appointments': appointments})

