from django.contrib import admin
from .models import MenuItem, Reservation


@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'is_signature', 'is_available')
    list_filter = ('category', 'is_signature', 'is_available')
    list_editable = ('is_available',)


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'date', 'time', 'party_size', 'is_cancelled')
    list_filter = ('is_cancelled', 'date')
    date_hierarchy = 'date'
