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


departments_names = {
            1: 'Developers',
            2: 'Programming',
            3: 'Technology',
            4: 'Customer Support'
        }


def welcome_page(request, *args, **kwargs):
    # return HttpResponse("<h1>Welcome to My site</h1>")
    return render(request, 'homepage.html')


def show_department_by_id(request, department_id):
    if department_id not in departments_names:
        context = {
            'id': department_id
        }
        return render(request, 'invalid_department.html', context)
    else:
        context = {
            'department_to_show': departments_names[department_id]
        }

    # return HttpResponse(f"<h1>Welcome to {departments_names[department_id]}</h1>")
    return render(request, 'department.html', context)


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


def crud_page(request):
    context = """
        <div>Click on operation to continue...
            <ul>
                <li><a href="http://localhost:8000/department/CRUD/create">Create</a></li>
                <li><a href="http://localhost:8000/department/CRUD/edit">Edit</a></li>
                <li><a href="http://localhost:8000/department/CRUD/delete">Delete</a></li>
            </ul>
        </div>
    """
    return HttpResponse(context)
