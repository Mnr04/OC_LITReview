from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='reviews/login.html'), name='login'),
]
