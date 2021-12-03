from django.shortcuts import render
from random import randint

# Create your views here.


def check_random(request):
    show_color = "#%06x" % randint(0, 0xFFFFFF)
    return render(request, 'color.html', {'check_random': show_color})




