import shutil
import os
from geobricks_data_manager.utils.log import logger
from geobricks_geoserver_manager.core.geoserver_manager_core import GeoserverManager
from geobricks_metadata_manager.core.metadata_manager_d3s_core import MetadataManager
from geobricks_data_manager.core.metadata_bridge import translate_from_metadata_to_geoserver, add_metadata_from_raster

log = logger(__file__)


class DataManager():

    metadata_manager = None
    geoserver_manager = None

    def __init__(self, config):
        # settings
        self.config = config

        # TODO: add only stuff used by Metadata manager?
        self.metadata_manager = MetadataManager(config)
        # TODO: add only stuff used by Geoserver manager?
        self.geoserver_manager = GeoserverManager(config)

    # PUBLISH

    def publish_data(self, data):
        print "switch to raster or vector"

    def publish_coveragestore(self, file_path, metadata_def, overwrite=False, publish_on_geoserver=True, publish_metadata=True, remove_file=False):
        """
        :param file_path: path to the input file
        :param metadata_def: json metadata
        :param overwrite: overwrite the resource
        :param publish_on_geoserver: publishing on Geoserver
        :param publish_metadata:  publishing on Metadata DB
        :param remove_file: remove the file the process is finished
        :return: ?
        """
        log.info("publish_coveragestore")
        try:
            # add additional layer info to the metadata i.e. bbox and EPSG code if they are not already added
            add_metadata_from_raster(file_path, metadata_def)
            # publish the coverage store
            return self._publish_coverage(file_path, metadata_def, overwrite, publish_on_geoserver, publish_metadata, remove_file)
        except Exception, e:
            raise Exception(e)

    def _publish_coverage(self, file_path, metadata_def=None, overwrite=False, publish_on_geoserver=True, publish_metadata=True, remove_file=False):
        """
        :param file_path: path to the input file
        :param metadata_def: json metadata
        :param overwrite: overwrite the resource
        :param publish_on_geoserver: publishing on Geoserver
        :param publish_metadata:  publishing on Metadata DB
        :param remove_file: remove the file the process is finished
        :return: ?
        """
        try:
            # get the title, if EN exists otherwise get the first available key TODO: how to do it better? default language?
            title = metadata_def["title"]["EN"] if "EN" in metadata_def["title"] else metadata_def["title"][metadata_def["title"].keys()[0]]

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
                log.info("Metadata published")

            # publish table on geoserver cluster
            if publish_on_geoserver is True:
                self.geoserver_manager.publish_coveragestore(file_path, geoserver_def, overwrite)
                log.info("Geoserver published")

            # remove files and folder of the shapefile
            if file_path is not None and remove_file:
                removefile(file_path)

        except Exception, e:
            log.error(e)
            self.rollback_coveragestore()

    def publish_codelist(self):
        # if a code doesn't exist publish a new code associate to the codelist (TODO: How to hanglde the labels?)
        log.warn('TODO Implement it for "meSpatialRepresentation":{"processing": {"idCodeList": "FENIX_GeographicalProcessing", "version" : "1.0", "codes": [{"code": "AVG_MONTHLY"}]}')
        log.warn('TODO Implement it for "meContent":{"resourceRepresentationType":"geographic","seCoverage":{"coverageSectors":{"idCodeList":"FENIX_GeographicalSectors","version":"1.0","codes":[{"code":"MODIS_LAND_COVER"}]}}')

    def publish_featuretype(self, data):
        print "publish_featuretype"

    def pulish_postgis_table(self, data):
        print "publish_featuretype"


    # DELETE

    def delete(self, uid, type, delete_on_geoserver=True, delete_metadata=True):
        log.warn("To implement")

    def delete_coveragestore(self, uid, delete_on_geoserver=True, delete_metadata=True):
        '''
        :param uid: resource uid of the coveragestore
        :param delete_on_geoserver: delete the resource from Geoserver
        :param delete_metadata:  delete the resource from Metadata DB
        :return: ?
        '''
        if delete_metadata:
            self.metadata_manager.delete_metadata(uid)
            log.info("Metadata removed: " + uid)
        # get layername from uid
        if delete_on_geoserver:
            layername = uid if "|" not in uid else uid.split("|")[1]
            self.geoserver_manager.delete_store(layername)
            log.info("Geoserver coveragestore removed: " + layername)


    def delete_featuretype(self, uid, delete_on_geoserver=True, delete_metadata=True):
        '''
        :param uid: resource uid of the featuretype (layer)
        :param delete_on_geoserver: delete the resource from Geoserver
        :param delete_metadata:  delete the resource from Metadata DB
        :return: ?
        '''
        try:
            if delete_metadata:
                self.metadata_manager.delete_metadata(uid)
                log.info("Metadata removed:" + uid)
        except Exception, e:
            log.error(e)
            raise Exception(e)

        try:
            if delete_on_geoserver:
                layername = uid if "|" not in uid else uid.split("|")[1]
                #TODO: shouldn't be passed also the workspace to gsconfig delete?
                self.geoserver_manager.delete_layer(layername)
                log.info("Geoserver layer removed: " + layername)
        except Exception, e:
            log.error(e)
            raise Exception(e)

    # SEARCH
    def get_all_layers(self):
        '''
        :return: json containing the stored layers
        '''
        return self.metadata_manager.get_all_layers()

    def get_metadata_by_uid(self, uid):
        '''
        :param uid: uid of the resource
        :return: json containing the stored metadata
        '''
        return self.metadata_manager.get_by_uid(uid)


    # ROLLBACK
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