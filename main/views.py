import json

from django.shortcuts import render
from django.http import JsonResponse
from main.forms import EmailAccessForm


def main(request):
    return render(request, 'index.html')


def register_email(request):
    if request.is_ajax() and request.method == 'POST':
        email_form = EmailAccessForm({'email': json.loads(request.body).get('email')})
        if email_form.is_valid():
            email_form.save()
            return JsonResponse({'message': 'Your email was saved, we will inform you soon about first version'})
    return JsonResponse({'message': 'Invalid email'})
