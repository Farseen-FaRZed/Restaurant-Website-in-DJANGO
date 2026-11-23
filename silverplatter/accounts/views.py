from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect

from .forms import SignUpForm, ProfileForm
from .models import User
from restaurant.models import Reservation


class SilverPlatterLoginView(LoginView):
    """Just Django's normal login view, pointed at our own template."""
    template_name = 'accounts/login.html'
    redirect_authenticated_user = True


def signup(request):
    if request.user.is_authenticated:
        return redirect('accounts:dashboard')

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f'Welcome to Silver Platter, {user.first_name}!')
            return redirect('accounts:dashboard')
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, "You've been logged out. See you again soon.")
    return redirect('restaurant:home')


@login_required
def dashboard(request):
    """
    One dashboard view for everyone - what it shows depends on the
    logged-in user's role:
      - Admins get sent straight to the Django admin panel.
      - Managers see every upcoming reservation.
      - Customers see just their own reservations.
    """
    user = request.user

    if user.role == User.ADMIN:
        return redirect('/admin/')

    if user.role == User.MANAGER:
        reservations = Reservation.objects.filter(is_cancelled=False).order_by('date', 'time')
        return render(request, 'accounts/dashboard.html', {
            'reservations': reservations,
            'is_manager': True,
        })

    # Customer
    reservations = user.reservations.filter(is_cancelled=False).order_by('date', 'time')
    return render(request, 'accounts/dashboard.html', {
        'reservations': reservations,
        'is_manager': False,
    })


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated.')
            return redirect('accounts:profile')
    else:
        form = ProfileForm(instance=request.user)
    return render(request, 'accounts/profile.html', {'form': form})
