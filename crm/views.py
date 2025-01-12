from django.shortcuts import render
from .models import Order

def table_page(request):
    object_list = Order.objects.all()
    return render(request, './index.html', {'object_list' : object_list})
