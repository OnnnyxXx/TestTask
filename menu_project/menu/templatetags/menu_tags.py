from django import template

from menu.models import MenuItem

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    menu_items = MenuItem.objects.filter(parent__isnull=True).prefetch_related('children')
    context['menu_items'] = menu_items
    context['menu_name'] = menu_name
    return ''
