from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import ReservationForm
from .models import MenuItem, Reservation


# --- Public pages -----------------------------------------------------------

def home(request):
    signature_dishes = MenuItem.objects.filter(is_signature=True, is_available=True)[:3]
    return render(request, 'restaurant/home.html', {'signature_dishes': signature_dishes})


def about(request):
    return render(request, 'restaurant/about.html')


def contact(request):
    if request.method == 'POST':
        # This is a simple demo form - it doesn't send a real email yet.
        # Once you have an email service set up, send the message from here.
        name = request.POST.get('name', '').strip()
        messages.success(request, f"Thank you, {name or 'friend'} — we'll be in touch shortly.")
        return redirect('restaurant:contact')
    return render(request, 'restaurant/contact.html')


def menu_list(request):
    items = MenuItem.objects.filter(is_available=True).order_by('category', 'name')

    # Group the dishes by category so the template can print each
    # section (Starters, Mains, Desserts) on its own.
    menu = {}
    for item in items:
        category_name = item.get_category_display()
        menu.setdefault(category_name, []).append(item)

    return render(request, 'restaurant/menu_list.html', {'menu': menu})


# --- Reservations ------------------------------------------------------------

@login_required
def book_reservation(request):
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            reservation.customer = request.user
            reservation.save()
            messages.success(request, 'Your table is booked and confirmed!')
            return redirect('accounts:dashboard')
    else:
        form = ReservationForm()

    return render(request, 'restaurant/book_reservation.html', {'form': form})


@login_required
def cancel_reservation(request, pk):
    """
    A customer can cancel their own reservation.
    A manager can cancel anyone's reservation (e.g. a no-show or a
    double-booking).
    """
    reservation = get_object_or_404(Reservation, pk=pk)
    is_owner = reservation.customer == request.user
    is_manager = request.user.role == 'MANAGER'

    if request.method == 'POST' and (is_owner or is_manager):
        reservation.is_cancelled = True
        reservation.save()
        messages.info(request, 'Reservation cancelled.')
    elif not (is_owner or is_manager):
        messages.error(request, "You can't cancel that reservation.")

    return redirect('accounts:dashboard')
