from django.shortcuts import render
from .models import *

# Create your views here.


def search_number(req):
    if req.method == 'POST':
        number = req.POST.get('number')
        if Sample.objects.filter(num=number).exists():
            result = "found"
        else:
            result = "not found"
        return render(req, 'index.html', {'result': result})
    return render(req, 'index.html')