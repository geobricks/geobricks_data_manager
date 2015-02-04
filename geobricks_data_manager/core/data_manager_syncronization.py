from geobricks_common.core.log import logger
from geobricks_common.core.filesystem import get_raster_path

log = logger(__file__)


def check_metadata(data_manager, check_geoserver=True, check_storage=True):
    '''
    This method checks the layer stored in the metadata and its consistency with the stored geoserver and storage layers
    :param data_manager: the configured DataManager instance
    :return: the list of missing layers
    '''
    geoserver_manager = data_manager.geoserver_manager
    layers = data_manager.get_all_layers()
    result = {}
    if check_geoserver:
        result["geoserver"] = _check_metadata_geoserver(geoserver_manager, layers)
    if check_storage:
        result["storage"] = _check_metadata_storage(layers)
    return result


def _check_metadata_geoserver(geoserver_manager, layers):
    result = []
    for layer in layers:
        # GeoServer consistency check
        if "datasource" in layer["dsd"]:
            if layer["dsd"]["datasource"] == "geoserver":
                #print layer["uid"], layer["dsd"]["datasource"]
                try:
                    layername = layer["dsd"]["layerName"]
                    workspace = layer["dsd"]["workspace"]
                    l = {
                        "layerName": layername,
                        "workspace": workspace,
                        "status": False
                    }
                    layer = geoserver_manager.gs_master.get_store(layername, workspace)
                    #log.info(workspace + ":" + layername + " " + str(layer))
                    l["status"] = True
                    result.append(l)
                except Exception, e:
                    log.error(e)
    return result

# TODO: to be implemented
def _check_metadata_storage(layers):
    result = []
    return result