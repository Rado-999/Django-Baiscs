from django.shortcuts import render, redirect

from FormsAdvanced.formdemo.forms import (MyModelForm, ModelForm2, PersonForm2,
                                          PersonFormSet, PersonForm)
from FormsAdvanced.formdemo.models import Person, ModelOne


def index(request):
    if request.method == "POST":
        form = MyModelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            cleaned_data = form.cleaned_data
            context = {
                'name': request.POST.get('name'),
                'age': request.POST.get('age'),
                'email': request.POST.get('email'),
                'persons': ModelOne.objects.all()
            }
            return render(request, 'created.html', context)
    else:
        form = MyModelForm()

    update_person_form = ModelForm2
    context = {
        'updated_form': update_person_form,
        'form': form,
        'modelfactory': PersonForm2,
        'person_form': PersonForm
    }
    return render(request, 'index.html', context)


def manage_people(request, ):
    if request.method == "POST":
        formset = PersonFormSet(request.POST, queryset=Person.objects.all())
        if formset.is_valid():
            formset.save()
            return redirect(index)

    else:
        formset = PersonFormSet(queryset=Person.objects.all())

    context = {
        'formset': formset
    }

    return render(request, 'manage.html', context)
