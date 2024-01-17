from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
# def index1(request, *args, **kwargs):
#     return HttpResponse("<h1>Welcome to department1 section</h1>")
#
#
# def index2(request, *args, **kwargs):
#     return HttpResponse("<h1>Welcome to department2 section</h1>")
#
#
# def index3(request, *args, **kwargs):
#     return HttpResponse("<h1>Welcome to department3 section</h1>")
#
#
# def index4(request, *args, **kwargs):
#     return HttpResponse("<h1>Welcome to department4 section</h1>")


def welcome_page(request, *args, **kwargs):
    return HttpResponse("<h1>Welcome to My site</h1>")


def show_department_by_id(request, department_id):
    return HttpResponse(f"<h1>Welcome to department {department_id} section</h1>")


def show_deparment_by_str(request, department_name):
    return HttpResponse(f"<h1>Welcome to department {department_name} section</h1>")


def show_deparment_by_slug(request, slug):
    return HttpResponse(f"<h1>Welcome to department {slug} section</h1>")


def create_department(request):
    return HttpResponse(f"<h1>Here u can create a new department</h1>")


def edit_department(request):
    return HttpResponse(f"<h1>Here u can edit an existing department</h1>")


def delete_department(request):
    return HttpResponse(f"<h1>Here u can delete an existing department</h1>")
