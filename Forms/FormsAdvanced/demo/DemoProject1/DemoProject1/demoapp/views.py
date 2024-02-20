from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import MyModelForm


# Create your views here.
def index(request):
    context = {
        'hello': 'page'
    }
    return render(request, 'Welcome.html', context)


#
#
# def form(request):
#     context = {
#         "modelform": MyModelForm(),
#     }
#
#     return render(request, "form.html", context)
#
#
# def created_view(request):
#     if request.method == 'GET':
#         context = {
#             'form': MyModelForm()
#         }
#
#         return render(request, "form.html", context)
#
#     else:
#         form = MyModelForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data['name'])
#             return render(request, "created_view.html")
#         else:
#             context={
#                 'form': form,
#                 'error_values': form.errors.items()
#             }
#             return error_view(request,context)
#
#
# def error_view(request,context):
#     errors = context['form'].errors
#     print(errors)
#     return render(request, "error.html",context)


def form_view(request):
    if request.method == 'POST':
        form = MyModelForm(request.POST)
        if form.is_valid():
            pass

    else:
        form = MyModelForm()

    context = {
        'form': form
    }

    return render(request, 'form.html', context)
