from django.shortcuts import render
from tethys_sdk.permissions import login_required
from tethys_sdk.gizmos import Button
from tethys_sdk.gizmos import PlotlyView
from django.http import HttpResponse, JsonResponse

from csv import writer as csv_writer
import plotly.graph_objs as go
import requests
import pandas as pd
import io

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

def get_observed_data_bs(request):
    """
    Get observed data from csv files in Hydroshare
    """

    get_data = request.GET

    try:

        codEstacion = get_data['code']
        nomEstacion = get_data['name']

        url = 'https://www.hydroshare.org/resource/d7d98390ab884eeda89f4a10b072bbc3/data/contents/BS/{}.csv'.format(codEstacion)

        s = requests.get(url).content

        df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=0)
        df.index = pd.to_datetime(df.index)

        datesBS = df.index.tolist()
        dataBS = df.iloc[:, 0].values
        dataBS.tolist()

        if isinstance(dataBS[0], str):
            dataBS = map(float, dataBS)

        observed_BS = go.Scatter(
            x=datesBS,
            y=dataBS,
            name='Solar Bright',
        )

        layout = go.Layout(title='Solar Bright at {0}-{1}'.format(nomEstacion, codEstacion),
                           xaxis=dict(title='Dates', ), yaxis=dict(title='Solar Bright (hours)',
                                                                   autorange=True), showlegend=False)

        chart_obj = PlotlyView(go.Figure(data=[observed_BS], layout=layout))

        context = {
            'gizmo_object': chart_obj,
        }

        return render(request, 'magdalena_cauca_data_viewer/gizmo_ajax.html', context)

    except Exception as e:
        print(str(e))
        return JsonResponse({'error': 'No data found for the selected station.'})

def get_observed_data_bs_csv(request):
    """
    Get observed data from csv files in Hydroshare
    """

    get_data = request.GET

    try:
        codEstacion = get_data['code']
        nomEstacion = get_data['name']

        url = 'https://www.hydroshare.org/resource/d7d98390ab884eeda89f4a10b072bbc3/data/contents/BS/{}.csv'.format(codEstacion)

        s = requests.get(url).content

        df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=0)
        df.index = pd.to_datetime(df.index)

        datesBS = df.index.tolist()
        dataBS = df.iloc[:, 0].values
        dataBS.tolist()

        pairs = [list(a) for a in zip(datesBS, dataBS)]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=solar_bright_{0}_{1}.csv'.format(codEstacion, nomEstacion)

        writer = csv_writer(response)
        writer.writerow(['datetime', 'solar bright (hours)'])

        for row_data in pairs:
            writer.writerow(row_data)

        return response

    except Exception as e:
        print(str(e))
        return JsonResponse({'error': 'An unknown error occurred while retrieving the Data.'})

def v_evaporation(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/v_evaporation.html', context)

def get_observed_data_ev(request):
    """
    Get observed data from csv files in Hydroshare
    """

    get_data = request.GET

    try:

        codEstacion = get_data['code']
        nomEstacion = get_data['name']

        url = 'https://www.hydroshare.org/resource/1021402cd2cb4519b3a02c3d9b2c3722/data/contents/EV/{}.csv'.format(codEstacion)

        s = requests.get(url).content

        df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=0)
        df.index = pd.to_datetime(df.index)

        datesEV = df.index.tolist()
        dataEV = df.iloc[:, 0].values
        dataEV.tolist()

        if isinstance(dataEV[0], str):
            dataEV = map(float, dataEV)

        observed_EV = go.Scatter(
            x=datesEV,
            y=dataEV,
            name='Evaporation',
        )

        layout = go.Layout(title='Evaporation at {0}-{1}'.format(nomEstacion, codEstacion),
                           xaxis=dict(title='Dates', ), yaxis=dict(title='Evaporation (mm)',
                                                                   autorange=True), showlegend=False)

        chart_obj = PlotlyView(go.Figure(data=[observed_EV], layout=layout))

        context = {
            'gizmo_object': chart_obj,
        }

        return render(request, 'magdalena_cauca_data_viewer/gizmo_ajax.html', context)

    except Exception as e:
        print(str(e))
        return JsonResponse({'error': 'No data found for the selected station.'})

def get_observed_data_ev_csv(request):
    """
    Get observed data from csv files in Hydroshare
    """

    get_data = request.GET

    try:
        codEstacion = get_data['code']
        nomEstacion = get_data['name']

        url = 'https://www.hydroshare.org/resource/1021402cd2cb4519b3a02c3d9b2c3722/data/contents/EV/{}.csv'.format(codEstacion)

        s = requests.get(url).content

        df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=0)
        df.index = pd.to_datetime(df.index)

        datesEV = df.index.tolist()
        dataEV = df.iloc[:, 0].values
        dataEV.tolist()

        pairs = [list(a) for a in zip(datesEV, dataEV)]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=evaporation_{0}_{1}.csv'.format(codEstacion, nomEstacion)

        writer = csv_writer(response)
        writer.writerow(['datetime', 'evaporation (mm)'])

        for row_data in pairs:
            writer.writerow(row_data)

        return response

    except Exception as e:
        print(str(e))
        return JsonResponse({'error': 'An unknown error occurred while retrieving the Data.'})


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