from django.shortcuts import render
from .models import Ubytovani


def index(request):
    context = {
        'nadpis': 'Ubytovací zařízení',
        'mista': Ubytovani.objects.all()
    }
    return render(request, 'index.html', context=context)
