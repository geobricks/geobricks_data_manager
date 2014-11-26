import shutil
import os
from geobricks_data_manager.utils.log import logger
from geobricks_geoserver_manager.core.geoserver_manager_core import GeoserverManager
from geobricks_metadata_manager.core.metadata_manager_d3s_core import MetadataManager
from geobricks_data_manager.core.metadata_bridge import translate_from_metadata_to_geoserver, add_metadata_from_raster

log = logger("geobricks_data_manager.data_manager_core")


class DataManager():

    metadata_manager = None
    geoserver_manager = None

    def __init__(self, config):
        # settings
        self.config = config
        self.metadata_manager = MetadataManager(config["metadata"])
        self.geoserver_manager = GeoserverManager(config["geoserver"])

    def publish_data(self, data):
        print "switch to raster or vector"

    def publish_coveragestore(self, file_path, metadata_def, overwrite=False, publish_on_geoserver=True, publish_metadata=True, remove_file=False):
        """
        @param file_path:
        @param metadata_def:
        @param overwrite:
        @return:
        """
        try:
            # add additional layer info to the metadata i.e. bbox and EPSG code
            add_metadata_from_raster(file_path, metadata_def)
            # add additional layer info to the metadata i.e. bbox and EPSG code
            self._publish_coverage(file_path, metadata_def, overwrite, publish_on_geoserver, publish_metadata, remove_file)
        except Exception, e:
            raise Exception(e)

    def _publish_coverage(self, file_path, metadata_def=None, overwrite=False, publish_on_geoserver=True, publish_metadata=True, remove_file=False):
        """
        @param file_path:
        @param layer_def:
        @param overwrite:
        @return:
        """
        try:
            # get the title, if EN exists otherwise get the first available key TODO: how to do it better? default language?
            title = metadata_def["title"]["EN"] if "EN" in metadata_def["title"] else  metadata_def["title"][metadata_def["title"].keys()[0]]

            # sanitize the layername. "layerName" has to be set
            metadata_def["dsd"]["layerName"] = sanitize_name(metadata_def["dsd"]["layerName"])
            layername = metadata_def["dsd"]["layerName"]

            # getting the default workspace
            metadata_def["dsd"]["workspace"] = metadata_def["dsd"]["workspace"] if "workspace" in metadata_def["dsd"] else self.geoserver_manager.get_default_workspace_name()

            # setting up the uid
            if "uid" not in metadata_def:
                metadata_def["uid"] = metadata_def["dsd"]["workspace"] + "|" + layername

            # setting up geoserver metadata TODO: move it
            abstact = None
            defaultStyle = None
            try: abstact = metadata_def["meContent"]["description"]["EN"]
            except Exception: pass
            try: defaultStyle = metadata_def["dsd"]["defaultStyle"]
            except Exception: pass
            geoserver_def = translate_from_metadata_to_geoserver(layername, title, metadata_def["dsd"]["workspace"], defaultStyle, abstact)

            # publish on metadata
            if publish_metadata is True:
                log.info(metadata_def)
                self.metadata_manager.publish_metadata(metadata_def, overwrite)

            # publish table on geoserver cluster
            if publish_on_geoserver is True:
                self.geoserver_manager.publish_coveragestore(file_path, geoserver_def, overwrite)

            # remove files and folder of the shapefile
            if file_path is not None and remove_file:
                removefile(file_path)

        except Exception, e:
            log.error(e)
            self.rollback_coveragestore()

    def publish_featuretype(self, data):
        print "publish_featuretype"


    def rollback_coveragestore(self):
        return "TODO rollback_coveragestore"


def sanitize_name(name):
    """
    This method clean the name of a layer, should be avoided to use dots as names
    :param name: name of the layer
    :return: sanitized layer name
    """
    name = name.replace(".", "")
    name = name.replace(" ", "_")
    name = name.lower()
    return name


def removefile(file_path):
    if os.path.isfile(file_path):
        os.remove(file_path)