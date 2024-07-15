from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .models import Trip, Vehicle, Branch

@login_required
def trips(request):
    trips = Trip.objects.all()

    return render(request, 'trips/trips.html', {
        'trips': trips
    })

@login_required
def trip(request, pk):
    trip = Trip.objects.get(pk=pk)

    return render(request, 'trips/trip.html', {
        'trip': trip
    })

@login_required
def add(request):
    if request.method == 'POST':
        vehicle_id = request.POST.get('vehicle', '')
        origin_id = request.POST.get('origin', '')
        destiny_id = request.POST.get('destiny', '')

        vehicle = Vehicle.objects.get(pk=vehicle_id)
        origin = Branch.objects.get(pk=origin_id)
        destiny = Branch.objects.get(pk=destiny_id)

        if vehicle and origin and destiny:
            Trip.objects.create(vehicle=vehicle, origin=origin, destiny=destiny)

            return redirect('/trips/')
        else:
            print('Viagem inválida.')

    vehicles = Vehicle.objects.all()
    branches = Branch.objects.all()

    return render(request, 'trips/add.html', {
        'vehicles': vehicles,
        'branches': branches,
    })

@login_required
def completed(request, pk):
    trip = Trip.objects.get(pk=pk)

    trip.completed = True
    trip.save()

    return redirect('/trips/')

@login_required
def update(request, pk):
    trip = Trip.objects.get(pk=pk)

    if request.method == 'POST':
        vehicle_id = request.POST.get('vehicle', '')
        origin_id = request.POST.get('origin', '')
        destiny_id = request.POST.get('destiny', '')

        trip.vehicle_id = vehicle_id
        trip.origin_id = origin_id
        trip.destiny_id = destiny_id

        if trip.vehicle_id and trip.origin_id and trip.destiny_id:
            trip.save()

            return redirect('/trips/', pk=trip.pk)
        else:
            print('Alteração inválida.')

    vehicles = Vehicle.objects.all()
    branches = Branch.objects.all()

    return render(request, 'trips/update.html', {
        'vehicles': vehicles,
        'branches': branches,
        'trip': trip,
    })

    

@login_required
def delete(request, pk):
    trip = Trip.objects.get(pk=pk)
    trip.delete()

    return redirect('/trips/')