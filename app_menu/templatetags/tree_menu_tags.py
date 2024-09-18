from django import template
from app_menu.models import MenuItem
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag
def draw_menu(menu_name, current_url):
    menu_items = MenuItem.objects.filter(name=menu_name)
    if current_url != 'favicon.ico':
        menu, flag = render_menu(menu_items, current_url, True)
        return mark_safe(menu)


def render_menu(menu_items, current_url, flag):
    menu_html = '<ul>'
    for item in menu_items:
        if not flag:
            return menu_html, False
        menu_html += '<li>'
        menu_html += f'''<a href="http://127.0.0.1:8000/{
            item.url}">{item.name}</a>'''
        if item.url == current_url:
            if item.children.exists():
                menu_html += '<ul>'
                for child in item.children.all():
                    menu_html += '<li>'
                    menu_html += f'''<a href="http://127.0.0.1:8000/{
                        child.url}">{child.name}</a>'''
                    menu_html += '</li>'
                menu_html += '</ul>'
            return menu_html, False
        if item.children.exists():
            menu, flag = render_menu(item.children.all(), current_url, flag)
            menu_html += menu
        menu_html += '</li>'
    menu_html += '</ul>'
    return menu_html, flag
