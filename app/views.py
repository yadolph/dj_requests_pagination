import csv

from django.shortcuts import render_to_response, redirect
from django.urls import reverse
from django.core.paginator import Paginator

def index(request):
    return redirect(reverse(bus_stations))


def bus_stations(request):
    current_page = request.GET.get('page')
    if current_page == None:
        current_page = 1

    with open('data-398-2018-08-30.csv', encoding='cp1251') as f:
        bus_data = csv.DictReader(f)
        bus_data = list(bus_data)

    paginator = Paginator(bus_data, 10)
    bus_stations = paginator.get_page(current_page)

    if bus_stations.has_next():
        next_page = f'?page={bus_stations.next_page_number()}'
    else:
        next_page = None

    if bus_stations.has_previous():
        prev_page = f'?page={bus_stations.previous_page_number()}'
    else:
        prev_page = None

    return render_to_response('index.html', context={
        'bus_stations': bus_stations,
        'current_page': current_page,
        'prev_page_url': prev_page,
        'next_page_url': next_page,
    })

