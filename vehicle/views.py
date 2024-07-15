from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Vehicle

@login_required
def vehicles(request):
    vehicles = Vehicle.objects.all()

    return render(request, 'vehicles/vehicles.html', {
        'vehicles': vehicles
    })

@login_required
def vehicle(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)

    return render(request, 'vehicles/vehicle.html', {
        'vehicle': vehicle
    })

@login_required
def add(request):
    if request.method == 'POST':
        model = request.POST.get('model', '')
        plate = request.POST.get('plate', '')
        year = request.POST.get('year', '')

        if model and plate and year:
            Vehicle.objects.create(model=model, plate=plate, year=year)

            return redirect('/vehicles/')
        else:
            print('Veículo inválido.')

    return render(request, 'vehicles/add.html')

@login_required
def update(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    
    if request.method == 'POST':
        model = request.POST.get('model', '')
        plate = request.POST.get('plate', '')
        year = request.POST.get('year', '')

        print('metódo post')

        if model and plate and year:
            vehicle.model = model
            vehicle.plate = plate
            vehicle.year = year
            vehicle.save()

            print('tudo ok')

            return redirect('/vehicles/')
        else:
            print('Alteração inválida')

    return render(request, 'vehicles/update.html', {
        'vehicle': vehicle
    })

@login_required
def delete(request, pk):
    vehicle = Vehicle.objects.get(pk=pk)
    vehicle.delete()

    return redirect('/vehicles/')