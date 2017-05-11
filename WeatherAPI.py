import argparse
import json
import urllib2

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

