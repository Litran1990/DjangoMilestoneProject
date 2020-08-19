from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserLoginForm, UserRegistrationForm, \
    UserProfileForm, UserFootballForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .models import UserProfile, UserFootball

# Index Page
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


# Login Page
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


# Registration Page
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


# Profile Page
def profile(request):
    """A view to return the profile page"""

    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, "Profile successfully updated")
            return redirect(reverse('profile'))

        messages.error(request, "Failed to update profile. \
            Make sure your form is valid")
        return redirect(reverse('profile'))

    form = UserProfileForm(instance=profile)

    template = 'profile.html'
    context = {
        'form': form
    }

    return render(request, template, context)


# Fan Page
def fan(request):
    """A view to return the user football fan info page"""

    fan = get_object_or_404(UserFootball, user=request.user)

    if request.method == 'POST':
        fan_form = UserFootballForm(request.POST, instance=fan)
        if fan_form.is_valid():
            fan_form.save()
            messages.success(request, "Fan information \
                successfully updated")
            return redirect(reverse('fan'))

        messages.error(request, "Failed to update fan information. \
            Make sure your form is valid")
        return redirect(reverse('fan'))

    fan_form = UserFootballForm(instance=fan)

    template = 'fan.html'
    context = {
        'fan_form': fan_form
    }

    return render(request, template, context)


# Update Password
def change_password(request):
    """ A view used to update the user's password """

    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('password_reset_done')
        else:
            return redirect('password_reset')
    else:
        form = PasswordChangeForm(user=request.user)
        return render(request, 'registration/password_reset_form.html', {'form': form})
