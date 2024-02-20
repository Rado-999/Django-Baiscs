from django.http import HttpResponse
from django.shortcuts import render, redirect

from djangoProject.LearningForms import forms
from djangoProject.LearningForms.forms import StudentModelForm, StudentForm
from djangoProject.LearningForms.models import StudentModel


# Create your views here.

def update_student(request, pk):
    student = StudentModel.objects.get(pk=pk)
    if request.method == 'GET':
        studentform = StudentModelForm(instance=student)
    else:
        studentform = StudentModelForm(request.POST, instance=student)
        if studentform.is_valid():
            studentform.save()
            return redirect('index')

    context = {
        'student_form': studentform,
        'student_pk': student.pk,
    }

    return render(request, 'update.html', context)


def modelindex(request):
    studentmodel = StudentModelForm(request.POST or None)
    if request.method == 'POST':
        if studentmodel.is_valid():
            studentmodel.save()

    return redirect('index')


def index(request):
    modelform = StudentModelForm(request.POST or None)
    form = StudentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            cleaned_data = form.cleaned_data
            context = {
                'name': cleaned_data['name'],
                'last_name': cleaned_data['last_name'],
                'age': cleaned_data['age'],
                'description': cleaned_data['description']
            }
            print(cleaned_data)
            return render(request, 'created.html', context)

    else:
        context = {
            'form': form,
            'modelform': modelform,
            'students_list': StudentModel.objects.all()
        }

        return render(request, 'index.html', context)

    # if request.method == 'GET':
    #     context = {
    #         'form': forms.StudentForm()
    #     }
    #     return render(request, 'index.html', context)
    #
    # else:
    #     form = forms.StudentForm(request.POST)
    #     if form.is_valid():
    #         cleaned_data = form.cleaned_data
    #         context = {
    #             'name': cleaned_data['name'],
    #             'last_name': cleaned_data['last_name'],
    #             'age': cleaned_data['age'],
    #             'description': cleaned_data['description']
    #         }
    #         return render(request, 'created.html', context)
    #
    #     else:
    #         context = {
    #             'form':form
    #         }
    #
    #         return render(request, 'error.html', context)
