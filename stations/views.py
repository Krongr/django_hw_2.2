from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse
from pagination.settings import BUS_STATION_CSV
from csv import DictReader


def index(request):
    return redirect(reverse('bus_stations'))


def get_stations_from_file(file_name):
    stations = []
    with open(file_name, newline='', encoding='utf-8') as csvfile:
        reader = DictReader(csvfile)
        for row in reader:
            stations.append({
                'Name': row['Name'],
                'Street': row['Street'],
                'District': row['District']
            })
    return stations


def bus_stations(request):
    page_number = int(request.GET.get("page", 1))
    paginator = Paginator(
        get_stations_from_file(BUS_STATION_CSV),
        10
    )
    stations = paginator.get_page(page_number)
    context = {
        'bus_stations': stations,
        'page': stations
    }
    return render(request, 'stations/index.html', context)
