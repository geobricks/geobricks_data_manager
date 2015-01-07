import unittest
from geobricks_data_manager.config.config import config
from geobricks_data_manager.core.data_manager_core import DataManager


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
            "workspace": "fenix",
            "layerName": "layer_test"
        }
    }

    @classmethod
    def setUpClass(cls):
        cls.add_metadata_coverage()

    @classmethod
    def add_metadata_coverage(self):
        try:
            self.data_manager.publish_coveragestore(self.path, self.metadata, False, False, True)
        except Exception, e:
            print e
            pass

    def test_delete_coveragestore(self):
        print self.metadata["uid"]
        result = self.data_manager.delete(self.metadata["uid"], True, False, False)
        self.assertEqual(result, True)
        #print "here"


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(GeobricksTest)
    unittest.TextTestRunner(verbosity=2).run(suite)