from django.conf import settings
from django.db import models


class MenuItem(models.Model):
    """One dish or drink on the menu."""

    STARTER = 'STARTER'
    MAIN = 'MAIN'
    DESSERT = 'DESSERT'

    CATEGORY_CHOICES = [
        (STARTER, 'Starters'),
        (MAIN, 'Mains'),
        (DESSERT, 'Desserts'),
    ]

    name = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    is_signature = models.BooleanField(default=False, help_text="Chef's signature dish")
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Reservation(models.Model):
    """A booked table. Bookings are confirmed the moment they're made -
    no approval step needed."""

    customer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                                  related_name='reservations')
    date = models.DateField()
    time = models.TimeField()
    party_size = models.PositiveSmallIntegerField(default=2)
    special_requests = models.TextField(blank=True)
    is_cancelled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.customer} - {self.date} {self.time} (x{self.party_size})'
