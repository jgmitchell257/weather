import argparse
import requests

loc_data = {}
with open("data/zipcode.csv","r") as f:
    for line in f:
        ugly = line.split()
        clean_data = []
        for (a,b) in enumerate(ugly):
            columns = b.split(",")
            for (a,b) in enumerate(columns):
                clean = b.strip()
                clean_data.append(clean)
            if len(clean_data[0]) == 3:
                ZIPCODE = "00" + clean_data[0]
            if len(clean_data[0]) == 4:
                ZIPCODE = "00" + clean_data[0]
            else:
                ZIPCODE = clean_data[0]
            LATITUDE = clean_data[1]
            LONGITUDE = clean_data[2]
            loc_data[ZIPCODE] = [LATITUDE,LONGITUDE]


parser = argparse.ArgumentParser(
    prog = "weather",
    description = "Grabs weather forecast from National Weather Service")
parser.add_argument("zip_code", help="Zip code of the location you want to get")
args = parser.parse_args()
options = vars(args)
zipcode = options["zip_code"]

def get_lat_and_lon(zipcode,loc_data):
    lat = loc_data[zipcode][0]
    lon = loc_data[zipcode][1]
    coordinates = [lat,lon]
    return coordinates

def get_forecast_url(location):
    lat = location[0]
    lon = location[1]
    data_url = "https://api.weather.gov/points/" + lat + "," + lon
    raw_data = requests.get(data_url)
    raw_json = raw_data.json()
    forecast_url = raw_json["properties"]["forecast"]
    return forecast_url

def print_forecast(url):
    raw_forecast = requests.get(url)
    clean_forecast = raw_forecast.json()
    now = clean_forecast["properties"]["periods"][0]
    later = clean_forecast["properties"]["periods"][1]
    name = now["name"]
    temp = now["temperature"]
    details = now["detailedForecast"]
    lname = later["name"]
    ltemp = later["temperature"]
    ldetails = later["detailedForecast"]
    print(name, temp)
    print(details + "\n\n")
    print(lname, ltemp)
    print(ldetails)

location = get_lat_and_lon(zipcode,loc_data)
url = get_forecast_url(location)
print_forecast(url)
