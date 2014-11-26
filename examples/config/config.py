import logging

config = {

    # To be used by Flask: DEVELOPMENT ONLY
    "debug": True,

    # Flask host: DEVELOPMENT ONLY
    "host": "168.202.28.214",

    # Flask port: DEVELOPMENT ONLY
    "port": 5020,

    # Logging configurations
    "logging": {
        "level": logging.INFO,
        "format": "%(asctime)s | %(levelname)-8s | %(name)-20s | Line: %(lineno)-5d | %(message)s",
        "datefmt": "%d-%m-%Y | %H:%M:%s"
    },

    # Folders
    "folders": {
        "config": "config/",
        "tmp": "/home/vortex/Desktop/LAYERS/tmp",
        "data_providers": "data_providers/",
        "metadata": "metadata/",
        "stats": "stats/",
        "geoserver": "geoserver/",
        "metadata_templates": "metadata/templates/",
        # used on runtime statistics (for Published layers this is the Geoservers Cluster "datadir")
        "geoserver_datadir": "/home/vortex/programs/SERVERS/tomcat_geoservers/data/",
        #"geoserver_datadir": "/home/vortex/Desktop/LAYERS/GEOSERVER_TEST",
        "distribution": "/home/vortex/Desktop/LAYERS/DISTRIBUTION/"
    },

    # Databases
    "db": {
        # Spatial Database
        "spatial": {
            # default_db will search in the dbs["database"] as default option
            "dbname": "fenix",
            "host": "localhost",
            "port": "5432",
            "username": "fenix",
            "password": "Qwaszx",
            "schema": "spatial"
        },
        "stats": {
            "dbname": "fenix",
            "host": "localhost",
            "port": "5432",
            "username": "fenix",
            "password": "Qwaszx",
            "schema": "stats"
        }
    },

    # Geoserver
    "geoserver": {
        "geoserver_master": "http://168.202.28.214:9090/geoserver/rest",
        "geoserver_slaves": [],
        "username": "admin",
        "password": "geoserver",
        # TODO: didn't implemnent it yet

        "default_db" : {
            'db': "spatial",
            'datastore': "spatial",
        },
    },

    "geoserver_tmp": {
        "geoserver_master": "http://168.202.28.214:9090/geoserver/rest",
        "geoserver_wms": "http://168.202.28.214:9090/geoserver/wms",
        "geoserver_slaves": [],
        "username": "admin",
        "password": "geoserver",
        "default_workspace": "tmp"
    },


    # Metadata
    "metadata": {
        "url_create_metadata": "http://exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/metadata",
        "url_get_metadata_uid": "http://exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/metadata/uid/<uid>",
        "url_get_metadata": "http://exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/find"
    }

}