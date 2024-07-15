from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Branch

@login_required
def branchs(request):
    branchs = Branch.objects.all()

    return render(request, 'branchs/branchs.html', {
        'branchs': branchs
    })

@login_required
def branch(request, pk):
    branch = Branch.objects.get(pk=pk)

    return render(request, 'branchs/branch.html', {
        'branch': branch
    })

@login_required
def add(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        address = request.POST.get('address', '')

        if name and address:
            Branch.objects.create(name=name, address=address)

            return redirect('/branchs/')
        else:
            print('Filial inválida.')

    return render(request, 'branchs/add.html')

@login_required
def update(request, pk):
    print('Método HTTP:', request.method) 
    branch = Branch.objects.get(pk=pk)
    
    if request.method == 'POST':
        name = request.POST.get('name', '')
        address = request.POST.get('address', '')

        if name and address:
            branch.name = name
            branch.address = address
            branch.save()
            print('tudo ok')
            return redirect('/branchs/')
        else:
            print('Alteração inválida')

    return render(request, 'branchs/update.html', {
        'branch': branch
    })

@login_required
def delete(request, pk):
    branch = Branch.objects.get(pk=pk)
    branch.delete()

    return redirect('/branchs/')