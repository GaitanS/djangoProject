from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView


def index(request):
    return HttpResponse('Hello World')


def student(request):
    context = {
        'all_students': [
            {
                'name': 'Silviu',
                'is_olympic': True,
                'age': 20
            },
            {
                'name': 'Mircea',
                'is_olympic': False,
                'age': 24
            }
        ]
    }
    return render(request, 'home/all_students.html', context)


def cars(request):
    context = {
        'cars': [
            {
                'name': 'Volvo',
                'damaged': False,
                'year': '2020'
            },
            {
                'name': 'Dacia',
                'damaged': True,
                'year': '2018'

            }
        ]
    }
    return render(request, 'home/cars.html', context)


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'
