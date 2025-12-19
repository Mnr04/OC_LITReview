from django.contrib import admin
from reviews.models import User, Ticket


# Here we tell Django to display data in the admin panel

admin.site.register(User)
admin.site.register(Ticket)