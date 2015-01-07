import logging

config = {

    "settings": {
        # To be used by Flask: DEVELOPMENT ONLY
        "debug": True,

        # Flask host: DEVELOPMENT ONLY
        "host": "localhost",

        # Flask port: DEVELOPMENT ONLY
        "port": 5904,

        # Logging configurations
        "logging": {
            "level": logging.INFO,
            "format": "%(asctime)s | %(levelname)-8s | %(name)-20s | Line: %(lineno)-5d | %(message)s",
            "datefmt": "%d-%m-%Y | %H:%M:%s"
        },

        # Metadata
        "metadata": {
            "url_create_metadata": "http://fenix.fao.org/d3s_dev/msd/resources/metadata",
            "url_get_metadata_uid": "http://fenix.fao.org/d3s_dev/msd/resources/metadata/uid/<uid>",

            # delete metadata
            "url_delete_metadata": "http://fenix.fao.org/d3s_dev/msd/resources/metadata/uid/<uid>",

            # get metadata
            "url_get_metadata": "http://fenix.fao.org/d3s_dev/msd/resources/find",

            # coding system
            "url_create_coding_system": "http://fenix.fao.org/d3s_dev/msd/resources",
            "url_data_coding_system": "http://fenix.fao.org/d3s_dev/msd/resources/data/uid/<uid>"
        },

        # geoserver settings
        "geoserver": {
            "geoserver_master": "http://localhost:9090/geoserver/rest",
            "geoserver_slaves": [],
            "username": "admin",
            "password": "geoserver",
        }
    }
}
