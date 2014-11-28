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

        # metadata config
        "metadata": {
            "url_create_metadata": "//exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/metadata",
            "url_get_metadata_uid": "//exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/metadata/uid/<uid>",
            "url_get_metadata": "//exldvsdmxreg1.ext.fao.org:7788/v2/msd/resources/metadata/uid/<uid>"
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
