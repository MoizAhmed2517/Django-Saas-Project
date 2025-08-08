from django.contrib import admin
from django.urls import path

from auth import views as auth_views
from .views import home_page_view

urlpatterns = [
    path ("", home_page_view),
    path("login/", auth_views.login_view),
    path("register/", auth_views.register_view),
    path('admin/', admin.site.urls)
]
