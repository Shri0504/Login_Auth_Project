# login_app/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from .forms import RegistrationForm, LoginForm
from .models import CustomUser

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False  # Deactivate login_app until email is verified
            user.save()
            send_verification_email(user, request)
            return render(request, 'login_app/verify_email.html')
    else:
        form = RegistrationForm()
    return render(request, 'login_app/register.html', {'form': form})

def send_verification_email(user, request):
    current_site = get_current_site(request)
    subject = 'Activate Your login_app'
    message = f"""
    Hi {user.username},
    Please click the link below to verify your email and activate your login_app:
    http://{current_site.domain}{reverse('login_app:verify', args=[urlsafe_base64_encode(force_bytes(user.pk)), default_token_generator.make_token(user)])}
    """
    send_mail(subject, message, 'your_email@gmail.com', [user.email])

def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = CustomUser.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
        user = None
    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.is_email_verified = True
        user.save()
        return render(request, 'login_app/verification_success.html')
    else:
        return render(request, 'login_app/verification_failed.html')

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            return redirect('login_app:dashboard')
    else:
        form = LoginForm()
    return render(request, 'login_app/login.html', {'form': form})

@login_required
def dashboard(request):
    return render(request, 'login_app/dashboard.html')
