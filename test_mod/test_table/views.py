from django.shortcuts import render
from django.http import HttpResponse
from .models import Imginfo


def table_view(request):
    context = {
            'img_data': Imginfo.objects.all()
    }
    return render(request, 'test_table/table.html', context)

