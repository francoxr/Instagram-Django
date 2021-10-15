"""Platzigram views"""

# Django
from django import http
from django.http import HttpResponse
from django.http import JsonResponse

# Utilities
from datetime import datetime

def hello_world(request):
    """Return a greeting."""
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse('Hi! Currente server time is {now}'.format(
        now=now)
        )

def sorted_numbers(request):
    """Hi."""
    numbers = request.GET['numbers']
    numbers_split = numbers.split(',')
    numbers_int= [int(number) for number in numbers_split]
    numbers_sorted = sorted(numbers_int)

    data = {
        "status_code": 200,
        "sorted": numbers_sorted
    }

    return JsonResponse(data)

def say_hi(request, name, age):
    """Return a greeting conditioanl"""
    if age <= 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)

    return HttpResponse(message)
