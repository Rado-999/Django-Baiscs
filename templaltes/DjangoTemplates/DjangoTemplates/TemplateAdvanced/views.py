from django.shortcuts import render


# Create your views here.


def home_page_view(request):
    return render(request, 'home.html', )


def user_page_view(request):
    context = {
        'nums': [1, 2, 3, 4, 5, 6]
    }
    return render(request, 'user.html', context)
