from tethys_sdk.base import TethysAppBase, url_map_maker


class MagdalenaCaucaDataViewer(TethysAppBase):
    """
    Tethys app class for Magdalena and Cauca Rivers Basin Data Viewer.
    """

    name = 'Magdalena and Cauca Rivers Basin Data Viewer'
    index = 'magdalena_cauca_data_viewer:home'
    icon = 'magdalena_cauca_data_viewer/images/logo_Magdalena_Cauca.png'
    package = 'magdalena_cauca_data_viewer'
    root_url = 'magdalena-cauca-data-viewer'
    color = '#008B8B'
    description = ''
    tags = ''
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='magdalena-cauca-data-viewer',
                controller='magdalena_cauca_data_viewer.controllers.home'
            ),
            UrlMap(
                name='stations_data',
                url='magdalena-cauca-data-viewer/stations_data',
                controller='magdalena_cauca_data_viewer.controllers.stations_data'
            ),
            UrlMap(
                name='v_solar_bright',
                url='magdalena-cauca-data-viewer/v_solar_bright',
                controller='magdalena_cauca_data_viewer.controllers.v_solar_bright'
            ),
            UrlMap(
	            name='get_observed_data_bs',
	            url='magdalena-cauca-data-viewer/v_solar_bright/get-observed-data-bs',
	            controller='magdalena_cauca_data_viewer.controllers.get_observed_data_bs'
            ),
            UrlMap(
	            name='get_observed_data_bs_csv',
	            url='magdalena-cauca-data-viewer/v_solar_bright/get-observed-data-bs-csv',
	            controller='magdalena_cauca_data_viewer.controllers.get_observed_data_bs_csv'
            ),
            UrlMap(
                name='v_evaporation',
                url='magdalena-cauca-data-viewer/v_evaporation',
                controller='magdalena_cauca_data_viewer.controllers.v_evaporation'
            ),
            UrlMap(
                name='get_observed_data_ev',
                url='magdalena-cauca-data-viewer/v_evaporation/get-observed-data-ev',
                controller='magdalena_cauca_data_viewer.controllers.get_observed_data_ev'
            ),
            UrlMap(
                name='get_observed_data_ev_csv',
                url='magdalena-cauca-data-viewer/v_evaporation/get-observed-data-ev-csv',
                controller='magdalena_cauca_data_viewer.controllers.get_observed_data_ev_csv'
            ),
            UrlMap(
                name='v_relative_humidity',
                url='magdalena-cauca-data-viewer/v_relative_humidity',
                controller='magdalena_cauca_data_viewer.controllers.v_relative_humidity'
            ),
            UrlMap(
                name='v_precipitation',
                url='magdalena-cauca-data-viewer/v_precipitation',
                controller='magdalena_cauca_data_viewer.controllers.v_precipitation'
            ),
            UrlMap(
                name='v_max_temperature',
                url='magdalena-cauca-data-viewer/v_max_temperature',
                controller='magdalena_cauca_data_viewer.controllers.v_max_temperature'
            ),
            UrlMap(
                name='v_min_temperature',
                url='magdalena-cauca-data-viewer/v_min_temperature',
                controller='magdalena_cauca_data_viewer.controllers.v_min_temperature'
            ),
            UrlMap(
                name='v_temperature',
                url='magdalena-cauca-data-viewer/v_temperature',
                controller='magdalena_cauca_data_viewer.controllers.v_temperature'
            ),
            UrlMap(
                name='raster_data',
                url='magdalena-cauca-data-viewer/raster_data',
                controller='magdalena_cauca_data_viewer.controllers.raster_data'
            ),
        )

        return url_maps