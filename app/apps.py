from django.apps import AppConfig


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib import messages


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

    def post(self, request):
        pass
