import unittest
import json
from geobricks_common.core.log import logger
from geobricks_data_manager.config.config import config
from geobricks_data_manager.core.data_manager_core import DataManager
from geobricks_data_manager.core.data_manager_syncronization import check_metadata

log = logger(__file__)

class GeobricksTest(unittest.TestCase):

    data_manager = DataManager(config)

    path = "../test_data/MODIS/MOD13A2/MOD13A2_3857.tif"
    metadata = {
        "uid": "test:layer_test",
        "title": {
            "EN": "TestLayer"
        },
        "meContent": {
            "resourceRepresentationType": "geographic",
        },
        "meSpatialRepresentation": {
            "layerType": "raster"
        },
        "dsd": {
            "contextSystem": "FENIX",
            "datasoruce" : "geoserver",
            "workspace": "test",
            "layerName": "layer_test"
        }
    }

    @classmethod
    def setUpClass(cls):
        cls.add_metadata_coverage()

    @classmethod
    def add_metadata_coverage(self):
        try:
            self.data_manager.publish_coveragestore(self.path, self.metadata)
        except Exception, e:
            log.error(e)
            pass

    def test_delete_coveragestore(self):
        result = self.data_manager.delete(self.metadata["uid"])
        self.assertEqual(result, True)

    def test_check_metadata(self):
        result = check_metadata(self.data_manager)
        log.info(result)


def test_suite():
    suite = unittest.TestLoader().loadTestsFromTestCase(GeobricksTest)
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    test_suite()
