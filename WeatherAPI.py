import argparse
import json
import urllib2
import requests

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

def request(apikey, targets, sDate, eDate):
    dict = {"appKey":"b1658f18-9f42-4dad-9178-a1adbc2c5d86", "targets":"93551", "startDate":"2010-1-01", "endDate":"2010-1-02"}
    if apikey != '':
        dict["appKey"] = apikey
    if targets != '':
        dict["targets"] = targets
    if sDate != '':
        dict["startDate"] = sDate
    if eDate != '':
        dict["endDate"] = eDate
    parameters = ""
    for key in dict:
        parameters =  parameters + key + "=" + dict[key] + '&'
    url = 'http://et.water.ca.gov/api/data?' + parameters + 'dataItems=day-asce-eto,day-eto,day-precip&unitOfMeasure=M;prioritizeSCS=N'
    response = requests.get(url)

    if (response.ok):
        jData = json.loads(response.content)
        print (jData)
    else:
        response.raise_for_status()
