from django import http
from django.http import HttpResponse
from django.shortcuts import render

from djangoProject.tasks.models import Task


# def index(request):
#     name = request.GET.get('name', 'NONAME')
#
#     return http.HttpResponse('It works')
#
#

def index(request):
    tasks = Task.objects.all()

    tasks = tasks.filter(description__icontains='Room',)

    if not tasks:
        return http.HttpResponse('<h1>No tasks found!!!</h1>')

    result = []

    for task in tasks:
        result.append(f"""
        <li>
            <h2>{task.title}</h2>
            <p>{task.description}</p>
        """
                      )

        ul = f"<ul>{''.join(result)}</ul>"

        content = f"""
            <h1>{len(tasks)} Tasks </h1>
        {ul}
        """

    return HttpResponse(content)


