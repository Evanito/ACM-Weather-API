import argparse
import json
import urllib2
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
    # quit(1)
# End handling args
api_data = {}


def request(apikey, targets, sDate, eDate):
    arguments = {"appKey": "b1658f18-9f42-4dad-9178-a1adbc2c5d86", "targets": "93551", "startDate": "2010-1-01", "endDate": "2010-1-02"}
    if apikey != '':
        arguments["appKey"] = str(apikey)
    if targets != '':
        arguments["targets"] = str(targets)
    if sDate != '':
        arguments["startDate"] = str(sDate)
    if eDate != '':
        arguments["endDate"] = str(eDate)
    parameters = ""
    for key in arguments:
        parameters = str(parameters) + str(key) + "=" + str(arguments[key]) + '&'
    url = 'http://et.water.ca.gov/api/data?' + parameters + 'dataItems=day-asce-eto,day-eto,day-precip&unitOfMeasure=M;prioritizeSCS=N'
    api_response = urllib2.urlopen(url)
    response = json.loads(api_response.read())
    api_response.close()
    global api_data
    api_data = response


def timestamp():
    ts = time.time()
    return datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')


request("b1658f18-9f42-4dad-9178-a1adbc2c5d86",'93551',timestamp(),timestamp())


def handle_data(data):
    pass
    # TODO: Handle data, make relevant, etc.