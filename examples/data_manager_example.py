from examples.config.config import config
from geobricks_data_manager.core.data_manager_core import DataManager

metadata_def = {
    "creationDate": 1416221596000,
    "meContent": {
        "resourceRepresentationType": "geographic",
        "seCoverage": {
            "coverageSectors": {
                "idCodeList": "FENIX_GeographicalSectors",
                "version": "1.0",
                "codes": [{"code": "MODIS_LAND_COVER"}]
            },
            "coverageTime": {
                "to": 949276800000,
                "from": 946684800000
            }
        }
    },
    "meSpatialRepresentation": {
        "processing": {
            "idCodeList": "FENIX_GeographicalProcessing",
            "version" : "1.0",
            "codes": [{"code": "AVG_MONTHLY"}]
        },
        "seDefaultStyle": {"name": "ghg_cultivation_organic_soils_cropland"},
        "layerType": "vector"
    },
    "title": {"EN": "Cultivation Organic Soils - Croplands"},

    "dsd" : {
        "contextSystem": "FENIX",
        "workspace": "dajeforte",
        "layerName": "MOD13A2_385722",
        "defaultStyle": "raster_style_modis"
    }
}
path = "../test_data/MODIS/MOD13A2/MOD13A2_3857.tif"

data_manager = DataManager(config)
data_manager.publish_coveragestore(path, metadata_def)