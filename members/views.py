from django.shortcuts import render, get_object_or_404, redirect
from .models import Member
from .form import MemberForm


def create_members(request):
    form = MemberForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('members:list')

    return render(request, 'members/create.html', {'form': form})


def list_members(request):
    members = Member.objects.all()
    return render(request, 'members/list.html', {'members': members})


def details_members(request, id):
    members = Member.objects.get(id=id)
    context = {}
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            context['is_valid'] = True
            form = MemberForm()
    else:
        form = MemberForm()
    context['form'] = form
    context['members'] = members
    template_name = 'members/details.html'

    return render(request, template_name, context)


def update_members(request, id):
    members = Member.objects.get(id=id)
    form = MemberForm(request.POST or None, instance=members)

    if form.is_valid():
        form.save()
        return redirect('members:list')

    return render(request, 'members/update.html', {'form': form, 'members': members})


def delete_members(request, id):
    members = Member.objects.get(id=id)

    if request.method == 'POST':
        members.delete()
        return redirect('members:list')

    return render(request, 'members/delete-confirm.html', {'members': members})
