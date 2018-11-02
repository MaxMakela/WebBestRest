import googlemaps
import pdb
import json
import time
import os

gmaps = googlemaps.Client(key=os.environ['GOOGLE_API_KEY'])

def get_rest_list(gmaps, place, page_id=None):
    result = gmaps.geocode(place)

    loc = result[0]['geometry']['location']
    pl = gmaps.places_nearby(loc, 5000, type='restaurant', page_token=page_id)
    next_page_token = pl.get('next_page_token')
    rest_list = [pl['results'], next_page_token]

    return json.dumps(rest_list)
