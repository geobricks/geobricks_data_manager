from setuptools import setup
from setuptools import find_packages

setup(
    name='GeobricksDataManager',
    version='0.0.1',
    author='Simone Murzilli; Guido Barbaglia',
    author_email='geobrickspy@gmail.com',
    packages=find_packages(),
    license='LICENSE.txt',
    long_description=open('README.md').read(),
    description='Geobricks library to handle Geoserver clusters and Metadata.',
    install_requires=[
        'flask',
        'GeobricksMetadataManager',
        'GeobricksGeoserverManager',
    ],
    url='http://pypi.python.org/pypi/GeobricksDataManager/',
    keywords=['geobricks', 'metadata', 'geoserver', 'd3s']
)
