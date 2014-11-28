import unittest
from config.config_test import config
from geobricks_data_manager.core.data_manager_core import DataManager

metadata_publish = {
    "uid": "fenix|layer_test",
    "meContent": {
        "resourceRepresentationType": "geographic",
    },
    "dsd": {
        "contextSystem": "FENIX",
        "workspace": "fenix",
        "layerName": "layer_test"
    }
}


class GeobricksTest(unittest.TestCase):

    def test_publish_coveragestore(self):
        print "here"

