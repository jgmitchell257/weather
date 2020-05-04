# Read me
Simple CLI app to pull and display data from the National Weather Service API

## Basic usage
usage: weather [-h] zip_code

Grabs weather forecast from National Weather Service

positional arguments:
  zip_code    Zip code of the location you want to get

optional arguments:
  -h, --help  show this help message and exit
 
 ## Data sources
Location data is from US Census data
* main link: https://www.census.gov/geographies/reference-files/time-series/geo/gazetteer-files.html
* Source file: https://www2.census.gov/geo/docs/maps-data/data/gazetteer/2019_Gazetteer/2019_Gaz_zcta_national.zip

Original file is included in the data folder
