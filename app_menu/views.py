from django.shortcuts import render


def draw_menu(request, item_url):
    return render(request, 'app_menu/menu.html', {'item_url': item_url})
