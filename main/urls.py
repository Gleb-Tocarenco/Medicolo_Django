from django.urls import re_path

from main.views import main, register_email


urlpatterns = [
    re_path(r'^$', main, name='main'),
    re_path(r'^early-access/$', register_email, name='main'),
]
