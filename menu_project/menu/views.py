from django.shortcuts import render
from .models import MenuItem


def menu(request):
    menu_items = MenuItem.objects.filter(parent__isnull=True).prefetch_related('children')
    context = {
        'menu_items': menu_items
    }
    return render(request, 'menu_template.html',  context)
