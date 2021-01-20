from django.shortcuts import render, redirect, get_object_or_404
from .models import Instructor
from .form import InstructorForm


def details(request, id):
    instructors = Instructor.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form = InstructorForm()
    else:
        form = InstructorForm()
    context['form'] = form
    context['instructors'] = instructors
    template_name = 'instructors/details.html'

    return render(request, template_name, context)


def list_instructor(request):
    instructors = Instructor.objects.all()
    return render(request, 'instructors/list.html', {'instructors': instructors})


def create_instructor(request):
    form = InstructorForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('instructors:list')

    return render(request, 'instructors/create.html', {'form': form})


def update_instructor(request, id):
    instructors = Instructor.objects.get(id=id)
    form = InstructorForm(request.POST or None, instance=instructors)

    if form.is_valid():
        form.save()
        return redirect('instructors:list')

    return render(request, 'instructors/update.html', {'form': form, 'instructors': instructors})


def delete_instructor(request, id):
    instructors = Instructor.objects.get(id=id)

    if request.method == 'POST':
        instructors.delete()
        return redirect('instructors:list')

    return render(request, 'instructors/delete-confirm.html', {'instructors': instructors})
