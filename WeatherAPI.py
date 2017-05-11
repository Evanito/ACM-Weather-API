import argparse
import json
import urllib2
import requests
import time
import datetime

parser = argparse.ArgumentParser()  # Start args.
parser.add_argument("-tgt", "--target", help="Zip code of weather data to be retrieved.")
parser.add_argument("-api", "--apikey", help="User's CIMS API key.")
args = parser.parse_args()  # End args.
# Start handling args.
if args.target:
    target = str(args.target)
else:
    # Automatically geolocate the connecting IP
    f = urllib2.urlopen('http://freegeoip.net/json/')
    json_string = f.read()
    f.close()
    location = json.loads(json_string)
    location_city = location['city']
    location_zip = location['zip_code']
    target = location_zip
    print "Autodetected Zip: " + target 
if args.apikey:
    api_key = str(args.api_key)
else:
    print "ERROR: API-Key missing.\nExiting..."
    quit(1)
# End handling args
api_data = {}


def request(apikey, targets, sDate, eDate):
    parameters = {"appKey": "b1658f18-9f42-4dad-9178-a1adbc2c5d86", "targets": "93551", "startDate": "2010-1-01", "endDate": "2010-1-02"}
    if apikey != '':
        parameters["appKey"] = apikey
    if targets != '':
        parameters["targets"] = targets
    if sDate != '':
        parameters["startDate"] = sDate
    if eDate != '':
        parameters["endDate"] = eDate
    parameters = ""
    for key in parameters:
        parameters = parameters + key + "=" + parameters[key] + '&'
    url = 'http://et.water.ca.gov/api/data?' + parameters + 'dataItems=day-asce-eto,day-eto,day-precip&unitOfMeasure=E;prioritizeSCS=N'
    response = requests.get(url)

    if response.ok:
        jData = json.loads(response.content)
        global api_data
        api_data = jData
    else:
        response.raise_for_status()


def timestamp():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')


def handle_data(data):
    pass
    # TODO: Handle data, make relevant, etc.