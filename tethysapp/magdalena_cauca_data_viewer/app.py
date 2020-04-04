from tethys_sdk.base import TethysAppBase, url_map_maker


class MagdalenaCaucaDataViewer(TethysAppBase):
    """
    Tethys app class for Magdalena and Cauca Rivers Basin Data Viewer.
    """

    name = 'Magdalena and Cauca Rivers Basin Data Viewer'
    index = 'magdalena_cauca_data_viewer:home'
    icon = 'magdalena_cauca_data_viewer/images/icon.gif'
    package = 'magdalena_cauca_data_viewer'
    root_url = 'magdalena-cauca-data-viewer'
    color = '#2980b9'
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
        )

        return url_maps