
def translate_from_metadata_to_geoserver(layername, title, workspace, defaultStyle=None, abstract=None):
    geoserver_def = {}
    geoserver_def = {}
    geoserver_def["layerName"] = layername
    geoserver_def["title"] = title
    geoserver_def["workspace"] = workspace
    if abstract is not None:
        geoserver_def["abstract"] = abstract
    if defaultStyle is not None:
        geoserver_def["defaultStyle"]= defaultStyle
    return geoserver_def


# TODO: move it
def add_metadata_from_raster(file_path, metadata_def):
    pass
    #print "TODO add_metadata_from_raster"
    # try:
    #     autorityname, authoritycode = get_authority(file_path)
    #     # print autorityname
    #     # print authoritycode
    #     # TODO: add to the metadata the EPSG code
    #     #metadata_json["defaultStyle"]["name"] = metadata_json["meSpatialRepresentation"]["seDefaultStyle"]["name"]
    # except Exception, e:
    #     log.error(e)
    #     pass
        # get boundingbox and set it

def add_metadata_from_vector(file_path, metadata_json):
    return "TODO:"

def translate_from_geoserver_to_metadata(metadata_json):
    return "TODO:"