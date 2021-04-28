from django.shortcuts import render
from django.http import HttpResponseServerError, HttpResponseNotFound


def custom_handler404(request, exception):
    return HttpResponseNotFound('Такой страницы не существует!')


def custom_handler500(request):
    return HttpResponseServerError('Ошибка сервера!')


def main_view(request):
    return render(request, 'index.html')


def departure_view(request, departure):
    return render(request, 'departure.html')


def tour_view(request, id):
    return render(request, 'tour.html')
