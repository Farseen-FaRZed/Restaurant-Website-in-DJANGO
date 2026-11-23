# Silver Platter (Lite)

The 1st simple version of the Silver Platter website.

## How to run it

```bash
pip install -r requirements.txt
python manage.py runserver
```

Then open http://127.0.0.1:8000/

The database (`db.sqlite3`) already has some demo data in it. Log in with:

| Role     | Username   | Password           |
|----------|-----------|---------------------|
| Admin    | `admin`    | `SilverAdmin123!`   |
| Manager  | `manager`  | `SilverManager123!` |
| Customer | `customer` | `SilverGuest123!`   |


## How it's organized

Only 2 apps this time:

- **accounts/** — the User model (with a `role` field), and login/signup/dashboard pages.
- **restaurant/** — the menu, and the reservation booking system.


## How the roles work

- Anyone who signs up on the site becomes a **Customer**.
- To make someone a **Manager**, go to `/admin/`, open that user, and
  change their Role to Manager. Managers get their own simple dashboard
  where they can see and cancel any reservation.
- **Admins** are just Django superusers — they log in and go straight to
  `/admin/`, where they can edit the menu, users, and reservations
  directly. No separate admin dashboard needed.

## Where to change things

- Restaurant name/phone/address/hours → top of `silverplatter/settings.py`
  (the `SITE_CONFIG` dictionary).
- Colors and fonts → top of `static/css/style.css`.
- Menu items → `/admin/` (Restaurant → Menu items).
- Page text (hero, about, etc.) → the `.html` files in
  `restaurant/templates/restaurant/`.

## Notes

- Reservations are confirmed instantly.
- The contact form doesn't send a real email yet (there's a comment in
  `restaurant/views.py` showing where to add that later).
