from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """
    Our own User model, based on Django's built-in one, with one thing
    added: a `role` field so we know if someone is a Customer, a Manager,
    or an Admin.

    How roles work here (kept deliberately simple):
    - Everyone who signs up on the website becomes a CUSTOMER.
    - To make someone a MANAGER or ADMIN, an admin just edits that user
      in the Django admin panel (/admin/) and changes their role there.
    """

    CUSTOMER = 'CUSTOMER'
    MANAGER = 'MANAGER'
    ADMIN = 'ADMIN'

    ROLE_CHOICES = [
        (CUSTOMER, 'Customer'),
        (MANAGER, 'Manager'),
        (ADMIN, 'Admin'),
    ]

    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default=CUSTOMER)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return f'{self.username} ({self.role})'
