from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm, UserProfileForm, UserPayment
from .models import UserProfile, UserPayment

# Create your views here.

"""Index Page"""
def index(request):
    """Return the index.html file"""
    return render(request, 'index.html')

@login_required
def logout(request):
    """Log the user out"""
    auth.logout(request)
    messages.success(request, "You have successfully been logged out")
    return redirect(reverse('index'))


"""Login Page"""
def login(request):
    """Log the user in"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    if request.method == "POST":
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged in!")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect")
    else:
        login_form = UserLoginForm()
    return render(request, 'login.html', {"login_form": login_form})


"""Registration Page"""
def registration(request):
    """Render the registration page"""
    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == "POST":
        registration_form = UserRegistrationForm(request.POST)

        if registration_form.is_valid():
            registration_form.save()
            user = auth.authenticate(username=request.POST['username'],
                                    password=request.POST['password1'])
            print(user)
            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))
            else:
                messages.error(request, "Unable to register your account at this time")
    else:
        registration_form = UserRegistrationForm()

    return render(request, 'registration.html', {
        "registration_form": registration_form})


"""Profile Page"""
def profile(request):
    """A view to return the profile page"""

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, f'Profile successfully updated')
            return redirect(reverse('profile'))

        messages.error(request, 'Failed to update profile. Make sure your form is valid')
        return redirect(reverse('profile'))

    form = UserProfileForm(instance=profile)

    template = 'profile.html'
    context = {
        'form': form
    }

    return render(request, template, context)


"""Credit Card Info Page"""
def payment(request):
    """A view to return the credit card info page"""

    payment = get_object_or_404(UserPayment, user=request.user)

    if request.method == 'POST':
        payment_form = UserPayment(request.POST, instance=payment)
        if payment_form.is_valid():
            payment_form.save()
            messages.success(request, f'Credit card information successfully updated')
            return redirect(reverse('payment'))

        messages.error(request, 'Failed to credit card information. Make sure your form is valid')
        return redirect(reverse('payment'))

    payment_form = UserPayment(instance=payment)

    template = 'payment.html'
    context = {
        'payment_form': payment_form
    }

    return render(request, template, context)