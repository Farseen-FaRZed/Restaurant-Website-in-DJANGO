from django.contrib import admin
from django.urls import path, include

admin.site.site_header = 'Silver Platter — Admin'
admin.site.site_title = 'Silver Platter Admin'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('restaurant.urls')),
]
