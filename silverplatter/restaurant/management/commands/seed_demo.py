from django.core.management.base import BaseCommand
from accounts.models import User
from restaurant.models import MenuItem


class Command(BaseCommand):
    help = 'Creates a few demo accounts and some sample menu items.'

    def handle(self, *args, **options):
        # --- Demo accounts, one for each role ---
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin', email='admin@silverplatter.example',
                password='SilverAdmin123!', role=User.ADMIN,
            )
            self.stdout.write('Created admin    -> admin / SilverAdmin123!')

        if not User.objects.filter(username='manager').exists():
            manager = User(username='manager', email='manager@silverplatter.example',
                            first_name='Morgan', last_name='Reyes', role=User.MANAGER)
            manager.set_password('SilverManager123!')
            manager.save()
            self.stdout.write('Created manager  -> manager / SilverManager123!')

        if not User.objects.filter(username='customer').exists():
            customer = User(username='customer', email='customer@silverplatter.example',
                             first_name='Jordan', last_name='Lee', role=User.CUSTOMER)
            customer.set_password('SilverGuest123!')
            customer.save()
            self.stdout.write('Created customer -> customer / SilverGuest123!')

        # --- A short sample menu ---
        dishes = [
            ('Burrata & Heirloom Tomato', MenuItem.STARTER, 'Basil oil, aged balsamic, sourdough crumb', 18, True),
            ('Tuna Crudo', MenuItem.STARTER, 'Yuzu, chili oil, shaved fennel', 19, False),
            ('Dry-Aged Ribeye', MenuItem.MAIN, '28-day aged, bone marrow butter', 58, True),
            ('Wild Mushroom Risotto', MenuItem.MAIN, 'Parmesan, black truffle, chive oil', 32, True),
            ('Pan-Seared Halibut', MenuItem.MAIN, 'Brown butter, capers, charred lemon', 42, False),
            ('Dark Chocolate Fondant', MenuItem.DESSERT, 'Salted caramel, vanilla bean ice cream', 14, True),
            ('Basque Cheesecake', MenuItem.DESSERT, 'Burnt honey, seasonal berries', 13, False),
        ]
        for name, category, description, price, signature in dishes:
            MenuItem.objects.get_or_create(
                name=name,
                defaults=dict(category=category, description=description,
                              price=price, is_signature=signature),
            )

        self.stdout.write(self.style.SUCCESS(
            f'Done. {MenuItem.objects.count()} menu items ready.'
        ))
