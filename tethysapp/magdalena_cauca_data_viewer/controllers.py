from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/home.html', context)

def stations_data(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/stations_data.html', context)

def v_solar_bright(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/v_solar_bright.html', context)

def v_evaporation(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/v_evaporation.html', context)

def v_relative_humidity(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/v_relative_humidity.html', context)

def v_precipitation(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/v_precipitation.html', context)

def v_max_temperature(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/v_max_temperature.html', context)

def v_min_temperature(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/v_min_temperature.html', context)

def v_temperature(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/v_temperature.html', context)

def raster_data(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/raster_data.html', context)