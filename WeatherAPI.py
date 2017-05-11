import argparse

parser = argparse.ArgumentParser()  # Start args.
parser.add_argument("-tgt", "--target", help="Zip code of weather data to be retrieved.")
parser.add_argument("-api", "--apikey", help="User's CIMS API key.")
args = parser.parse_args()  # End args.
# Start handling args.
if args.target:
    target = str(args.target)
else:
    #  TODO: auto_target()
    pass
if args.apikey:
    api_key = str(args.api_key)
else:
    print "ERROR: API-Key missing.\nExiting..."
    quit(1)
# End handling args

