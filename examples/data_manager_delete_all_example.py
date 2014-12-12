from examples.config.config import config
from geobricks_data_manager.core.data_manager_core import DataManager

data_manager = DataManager(config)
layers = data_manager.get_all_layers()
for layer in layers:
    try:
        print layer["uid"]
        #data_manager.delete_coveragestore(layer["uid"])
    except Exception, e:
        print e
        pass


