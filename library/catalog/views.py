from django.shortcuts import render

# Create your views here.

from django.shortcuts import render


def get_info(request):
    info = {
        'title': 'Абра кадабра',
        'author': 'Лев Толстый',
        'year': 1984,
        'rating': 5
    }

    return render(request, 'catalog/book_detail.html', {'info': info})