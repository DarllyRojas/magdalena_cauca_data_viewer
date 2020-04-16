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
    Controller for the app Solar bright page.
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

        s = requests.get(url, verify=False).content

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

        s = requests.get(url, verify=False).content

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

        s = requests.get(url, verify=False).content

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

        s = requests.get(url, verify=False).content

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

def get_observed_data_hr(request):
    """
    Get observed data from csv files in Hydroshare
    """

    get_data = request.GET

    try:

        codEstacion = get_data['code']
        nomEstacion = get_data['name']

        url = 'https://www.hydroshare.org/resource/5ddb8470be904567af4f6b29434a5d51/data/contents/HR/{}.csv'.format(codEstacion)

        s = requests.get(url, verify=False).content

        df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=0)
        df.index = pd.to_datetime(df.index)

        datesHR = df.index.tolist()
        dataHR = df.iloc[:, 0].values
        dataHR.tolist()

        if isinstance(dataHR[0], str):
            dataHR = map(float, dataBS)

        observed_HR = go.Scatter(
            x=datesHR,
            y=dataHR,
            name='Relative Humidity',
        )

        layout = go.Layout(title='Relative Humidity at {0}-{1}'.format(nomEstacion, codEstacion),
                           xaxis=dict(title='Dates', ), yaxis=dict(title='Relative Humidity (%)',
                                                                   autorange=True), showlegend=False)

        chart_obj = PlotlyView(go.Figure(data=[observed_HR], layout=layout))

        context = {
            'gizmo_object': chart_obj,
        }

        return render(request, 'magdalena_cauca_data_viewer/gizmo_ajax.html', context)

    except Exception as e:
        print(str(e))
        return JsonResponse({'error': 'No data found for the selected station.'})

def get_observed_data_hr_csv(request):
    """
    Get observed data from csv files in Hydroshare
    """

    get_data = request.GET

    try:
        codEstacion = get_data['code']
        nomEstacion = get_data['name']

        url = 'https://www.hydroshare.org/resource/5ddb8470be904567af4f6b29434a5d51/data/contents/HR/{}.csv'.format(codEstacion)

        s = requests.get(url, verify=False).content

        df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=0)
        df.index = pd.to_datetime(df.index)

        datesHR = df.index.tolist()
        dataHR = df.iloc[:, 0].values
        dataHR.tolist()

        pairs = [list(a) for a in zip(datesHR, dataHR)]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=relative_humidity_{0}_{1}.csv'.format(codEstacion, nomEstacion)

        writer = csv_writer(response)
        writer.writerow(['datetime', 'relative humidiy (%)'])

        for row_data in pairs:
            writer.writerow(row_data)

        return response

    except Exception as e:
        print(str(e))
        return JsonResponse({'error': 'An unknown error occurred while retrieving the Data.'})


def v_precipitation(request):
    """
    Controller for the app precipitation page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/v_precipitation.html', context)

def get_observed_data_prec(request):
    """
    Get observed data from csv files in Hydroshare
    """

    get_data = request.GET

    try:

        codEstacion = get_data['code']
        nomEstacion = get_data['name']

        url = 'https://www.hydroshare.org/resource/7e1747a802cd42418e7f277ec10f91be/data/contents/PREC/{}.csv'.format(codEstacion)
        # Here change id resource for csv
        s = requests.get(url, verify=False).content

        df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=0)
        df.index = pd.to_datetime(df.index)

        datesPREC = df.index.tolist()
        dataPREC = df.iloc[:, 0].values
        dataPREC.tolist()

        if isinstance(dataPREC[0], str):
            dataPREC = map(float, dataPREC)

        observed_PREC = go.Scatter(
            x=datesPREC,
            y=dataPREC,
            name='Precipitation',
        )

        layout = go.Layout(title='Precipitation at {0}-{1}'.format(nomEstacion, codEstacion),
                           xaxis=dict(title='Dates', ), yaxis=dict(title='Precipitation (mm)',
                                                                   autorange=True), showlegend=False)

        chart_obj = PlotlyView(go.Figure(data=[observed_PREC], layout=layout))

        context = {
            'gizmo_object': chart_obj,
        }

        return render(request, 'magdalena_cauca_data_viewer/gizmo_ajax.html', context)

    except Exception as e:
        print(str(e))
        return JsonResponse({'error': 'No data found for the selected station.'})

def get_observed_data_prec_csv(request):
    """
    Get observed data from csv files in Hydroshare
    """

    get_data = request.GET

    try:
        codEstacion = get_data['code']
        nomEstacion = get_data['name']

        url = 'https://www.hydroshare.org/resource/7e1747a802cd42418e7f277ec10f91be/data/contents/PREC/{}.csv'.format(codEstacion)

        s = requests.get(url, verify=False).content

        df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=0)
        df.index = pd.to_datetime(df.index)

        datesPREC = df.index.tolist()
        dataPREC = df.iloc[:, 0].values
        dataPREC.tolist()

        pairs = [list(a) for a in zip(datesPREC, dataPREC)]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=precipitation_{0}_{1}.csv'.format(codEstacion, nomEstacion)

        writer = csv_writer(response)
        writer.writerow(['datetime', 'precipitation (mm)'])

        for row_data in pairs:
            writer.writerow(row_data)

        return response

    except Exception as e:
        print(str(e))
        return JsonResponse({'error': 'An unknown error occurred while retrieving the Data.'})


def v_max_temperature(request):
    """
    Controller for the app maximun temperature page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/v_max_temperature.html', context)

def get_observed_data_tmax(request):
    """
    Get observed data from csv files in Hydroshare
    """

    get_data = request.GET

    try:

        codEstacion = get_data['code']
        nomEstacion = get_data['name']

        url = 'https://www.hydroshare.org/resource/5cb3aebd67d04de7aba1e69cf1b6376c/data/contents/T_MAX/{}.csv'.format(codEstacion)

        s = requests.get(url, verify=False).content

        df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=0)
        df.index = pd.to_datetime(df.index)

        datesTMAX = df.index.tolist()
        dataTMAX = df.iloc[:, 0].values
        dataTMAX.tolist()

        if isinstance(dataTMAX[0], str):
            dataTMAX = map(float, dataTMAX)

        observed_TMAX = go.Scatter(
            x=datesTMAX,
            y=dataTMAX,
            name='Temperature',
        )

        layout = go.Layout(title='Maximum Temperature at {0}-{1}'.format(nomEstacion, codEstacion),
                           xaxis=dict(title='Dates', ), yaxis=dict(title='Maximum Temperature (°C)',
                                                                   autorange=True), showlegend=False)

        chart_obj = PlotlyView(go.Figure(data=[observed_TMAX], layout=layout))

        context = {
            'gizmo_object': chart_obj,
        }

        return render(request, 'magdalena_cauca_data_viewer/gizmo_ajax.html', context)

    except Exception as e:
        print(str(e))
        return JsonResponse({'error': 'No data found for the selected station.'})

def get_observed_data_tmax_csv(request):
    """
    Get observed data from csv files in Hydroshare
    """

    get_data = request.GET

    try:
        codEstacion = get_data['code']
        nomEstacion = get_data['name']

        url = 'https://www.hydroshare.org/resource/5cb3aebd67d04de7aba1e69cf1b6376c/data/contents/T_MAX/{}.csv'.format(codEstacion)

        s = requests.get(url, verify=False).content

        df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=0)
        df.index = pd.to_datetime(df.index)

        datesTMAX = df.index.tolist()
        dataTMAX = df.iloc[:, 0].values
        dataTMAX.tolist()

        pairs = [list(a) for a in zip(datesTMAX, dataTMAX)]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=T_max_{0}_{1}.csv'.format(codEstacion, nomEstacion)

        writer = csv_writer(response)
        writer.writerow(['datetime', 'Maximum temperature  (°C)'])

        for row_data in pairs:
            writer.writerow(row_data)

        return response

    except Exception as e:
        print(str(e))
        return JsonResponse({'error': 'An unknown error occurred while retrieving the Data.'})

def v_min_temperature(request):
    """
    Controller for the app Minimum page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/v_min_temperature.html', context)

def get_observed_data_tmin(request):
    """
    Get observed data from csv files in Hydroshare
    """

    get_data = request.GET

    try:

        codEstacion = get_data['code']
        nomEstacion = get_data['name']

        url = 'https://www.hydroshare.org/resource/3de9f32fa75c4b73b73ce8215b513cf7/data/contents/T_MIN/{}.csv'.format(codEstacion)

        s = requests.get(url, verify=False).content

        df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=0)
        df.index = pd.to_datetime(df.index)

        datesTMIN = df.index.tolist()
        dataTMIN= df.iloc[:, 0].values
        dataTMIN.tolist()

        if isinstance(dataTMIN[0], str):
            dataTMIN = map(float, dataTMIN)

        observed_TMIN = go.Scatter(
            x=datesTMIN,
            y=dataTMIN,
            name='Temperature',
        )

        layout = go.Layout(title='Minimum Temperature at {0}-{1}'.format(nomEstacion, codEstacion),
                           xaxis=dict(title='Dates', ), yaxis=dict(title='Minimum Temperature (°C)',
                                                                   autorange=True), showlegend=False)

        chart_obj = PlotlyView(go.Figure(data=[observed_TMIN], layout=layout))

        context = {
            'gizmo_object': chart_obj,
        }

        return render(request, 'magdalena_cauca_data_viewer/gizmo_ajax.html', context)

    except Exception as e:
        print(str(e))
        return JsonResponse({'error': 'No data found for the selected station.'})
def get_observed_data_tmin_csv(request):
    """
    Get observed data from csv files in Hydroshare
    """

    get_data = request.GET

    try:
        codEstacion = get_data['code']
        nomEstacion = get_data['name']

        url = 'https://www.hydroshare.org/resource/3de9f32fa75c4b73b73ce8215b513cf7/data/contents/T_MIN/{}.csv'.format(codEstacion)

        s = requests.get(url, verify=False).content

        df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=0)
        df.index = pd.to_datetime(df.index)

        datesTMIN = df.index.tolist()
        dataTMIN = df.iloc[:, 0].values
        dataTMIN.tolist()

        pairs = [list(a) for a in zip(datesTMIN, dataTMIN)]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=T_min_{0}_{1}.csv'.format(codEstacion, nomEstacion)

        writer = csv_writer(response)
        writer.writerow(['datetime', 'Minimum temperature  (°C)'])

        for row_data in pairs:
            writer.writerow(row_data)

        return response

    except Exception as e:
        print(str(e))
        return JsonResponse({'error': 'An unknown error occurred while retrieving the Data.'})


def v_temperature(request):
    """
    Controller for the app temperature page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/v_temperature.html', context)
def get_observed_data_temp(request):
    """
    Get observed data from csv files in Hydroshare
    """

    get_data = request.GET

    try:

        codEstacion = get_data['code']
        nomEstacion = get_data['name']

        url = 'https://www.hydroshare.org/resource/713d0a35bd2c48f8ba47c6fa76be2bac/data/contents/TEMP/{}.csv'.format(codEstacion)

        s = requests.get(url, verify=False).content

        df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=0)
        df.index = pd.to_datetime(df.index)

        datesTEMP = df.index.tolist()
        dataTEMP = df.iloc[:, 0].values
        dataTEMP.tolist()

        if isinstance(dataTEMP[0], str):
            dataTEMP = map(float, dataTEMP)

        observed_TEMP = go.Scatter(
            x=datesTEMP,
            y=dataTEMP,
            name='Temperature',
        )

        layout = go.Layout(title='Temperature at {0}-{1}'.format(nomEstacion, codEstacion),
                           xaxis=dict(title='Dates', ), yaxis=dict(title='Temperature (°C)',
                                                                   autorange=True), showlegend=False)

        chart_obj = PlotlyView(go.Figure(data=[observed_TEMP], layout=layout))

        context = {
            'gizmo_object': chart_obj,
        }

        return render(request, 'magdalena_cauca_data_viewer/gizmo_ajax.html', context)

    except Exception as e:
        print(str(e))
        return JsonResponse({'error': 'No data found for the selected station.'})
def get_observed_data_temp_csv(request):
    """
    Get observed data from csv files in Hydroshare
    """

    get_data = request.GET

    try:
        codEstacion = get_data['code']
        nomEstacion = get_data['name']

        url = 'https://www.hydroshare.org/resource/713d0a35bd2c48f8ba47c6fa76be2bac/data/contents/TEMP/{}.csv'.format(codEstacion)

        s = requests.get(url, verify=False).content

        df = pd.read_csv(io.StringIO(s.decode('utf-8')), index_col=0)
        df.index = pd.to_datetime(df.index)

        datesTEMP = df.index.tolist()
        dataTEMP = df.iloc[:, 0].values
        dataTEMP.tolist()

        pairs = [list(a) for a in zip(datesTEMP, dataTEMP)]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=temperature_{0}_{1}.csv'.format(codEstacion, nomEstacion)

        writer = csv_writer(response)
        writer.writerow(['datetime', 'temperature (°C)'])

        for row_data in pairs:
            writer.writerow(row_data)

        return response

    except Exception as e:
        print(str(e))
        return JsonResponse({'error': 'An unknown error occurred while retrieving the Data.'})


def raster_data(request):
    """
    Controller for the app home page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/raster_data.html', context)

def r_solar_bright(request):
    """
    Controller for the app Solar bright page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/r_solar_bright.html', context)

def r_evaporation(request):
    """
    Controller for the app Solar bright page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/r_evaporation.html', context)

def r_relative_humidity(request):
    """
    Controller for the app Solar bright page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/r_relative_humidity.html', context)

def r_precipitation(request):
    """
    Controller for the app Precipitation page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/r_precipitation.html', context)

def r_max_temperature(request):
    """
    Controller for the app Maximum Temperature page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/r_max_temperature.html', context)

def r_min_temperature(request):
    """
    Controller for the app Minimum Temperature page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/r_min_temperature.html', context)

def r_temperature(request):
    """
    Controller for the app Temperature page.
    """

    context = {
    }

    return render(request, 'magdalena_cauca_data_viewer/r_temperature.html', context)
