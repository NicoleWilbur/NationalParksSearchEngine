import json

import requests
import pandas as pd
import flat_table
from api_data import jprint
from decrypt_key import key_decryption


def dc(data):
    string = ""
    if not data:
        scrubbed = "No Data"
    elif isinstance(data, list):
        for i in data:
            string += i + " & "
        scrubbed = string[:-2]
    else:
        scrubbed = data
    return scrubbed


class APIPandas:

    def __init__(self):
        self.api_key = key_decryption()
        self.api_addresses = ["https://developer.nps.gov/api/v1/activities/parks?",
                              "https://developer.nps.gov/api/v1/amenities/parksplaces?",
                              "https://developer.nps.gov/api/v1/amenities/parksvisitorcenters?",
                              "https://developer.nps.gov/api/v1/campgrounds?",
                              "https://developer.nps.gov/api/v1/parkinglots?",
                              "https://developer.nps.gov/api/v1/places?",
                              "https://developer.nps.gov/api/v1/thingstodo?",
                              "https://developer.nps.gov/api/v1/topics/parks?"]
        #results = response.json()['data']

    def get_data(self):

        ##activities_parks
        cols = ["park_code", "park_name", "park_states", "activity_name"]
        data = []

        response = requests.get(self.api_addresses[0] + self.api_key)
        results = response.json()["data"]

        for item in results:
            for park in item['parks']:
                lst = [park['parkCode'], park['fullName'], park['states'], item['name']]
                #lst = [dc(park['parkCode']), dc(park['fullName']), dc(park['states']), dc(item['name'])]
                data.append(lst)
        activities_df = pd.DataFrame(data=data, columns=cols)
        #print(activities_df.to_string())

        ##amenities_parks
        cols = ["park_code", "amenity_name", "url"]
        data = []

        response = requests.get(self.api_addresses[1] + self.api_key)
        results = response.json()["data"]

        for item in results:
            for park in item[0]["parks"]:
                for place in park["places"]:
                    lst = [park["parkCode"], item[0]["name"], place["url"]]
                data.append(lst)
        amenities_parks_df = pd.DataFrame(data=data, columns=cols)
        #print(amenities_parks_df.to_string())

        ##amenities_visitor_centers
        cols = ["park_code", "amenity_name", "visitor_center_name", "visitor_center_url"]
        data = []

        response = requests.get(self.api_addresses[2] + self.api_key)
        results = response.json()["data"]

        for item in results:
            for park in item[0]["parks"]:
                for visitor_center in park['visitorcenters']:
                    lst = [park["parkCode"], item[0]["name"], visitor_center['name'], visitor_center['url']]
                data.append(lst)
        amenities_vc_df = pd.DataFrame(data=data, columns=cols)
        #print(amenities_vc_df.to_string())

        ##campgrounds
        cols = ["park_code", "paved_roads", "general_ADA", "campground_classification", "wheelchair_access_campground",
                "rv_allowed", "rv_info", "rv_max_length", "trailers_allowed", "trailer_max_length", "description", "campground_id",
                "campsite_name", "url", "cell_reception", "camp_store", "dump_station", "internet", "potable_water",
                "showers", "toilets", "campsites_electric", "campsites_group", "campsites_horse", "campsites_other",
                "campsites_rv_only", "campsites_tent_only", "campsites_boat_ramp", "total_sites", "staff_volunteer"]
        data = []

        response = requests.get(self.api_addresses[3] + self.api_key)
        results = response.json()["data"]

        jprint(results)

        for item in results:
            lst = [dc(item['parkCode']), dc(item['accessibility']['accessRoads']), dc(item['accessibility']['adaInfo']),
                   dc(item['accessibility']['classifications']), dc(item['accessibility']['wheelchairAccess']),
                   dc(item['accessibility']['rvAllowed']), dc(item['accessibility']['rvInfo']), dc(item['accessibility']['rvMaxLength']),
                   dc(item['accessibility']['trailerAllowed']), dc(item['accessibility']['trailerMaxLength']),
                   dc(item['description']), dc(item['id']), dc(item['name']), dc(item['url']), dc(item['amenities']['cellPhoneReception']),
                   dc(item['amenities']['campStore']), dc(item['amenities']['dumpStation']), dc(item['amenities']['internetConnectivity']),
                   dc(item['amenities']['potableWater']), dc(item['amenities']['showers']), dc(item['amenities']['toilets']),
                   dc(item['campsites']['electricalHookups']), dc(item['campsites']['group']), dc(item['campsites']['horse']),
                   dc(item['campsites']['other']), dc(item['campsites']['rvOnly']), dc(item['campsites']['tentOnly']),
                   dc(item['campsites']['walkBoatTo']), dc(item['campsites']['totalSites']),
                   dc(item['amenities']['staffOrVolunteerHostOnsite'])]

            data.append(lst)
        print(data)
        campgrounds_df = pd.DataFrame(data=data, columns=cols)
        print(campgrounds_df.to_string())


