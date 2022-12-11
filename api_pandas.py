import json
import requests
import pandas as pd
import flat_table
from api_data import jprint
from decrypt_key import key_decryption


class APIPandas:

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_addresses = ["https://developer.nps.gov/api/v1/activities/parks?limit=99000",
                              "https://developer.nps.gov/api/v1/amenities/parksplaces?limit=99000",
                              "https://developer.nps.gov/api/v1/amenities/parksvisitorcenters?limit=99000",
                              "https://developer.nps.gov/api/v1/campgrounds?limit=99000?",
                              "https://developer.nps.gov/api/v1/parkinglots?limit=99000",
                              "https://developer.nps.gov/api/v1/places?limit=99000",
                              "https://developer.nps.gov/api/v1/thingstodo?limit=99000",
                              "https://developer.nps.gov/api/v1/topics/parks?limit=99000"]
        # results = response.json()['data']

    @staticmethod
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

    def get_data(self):

        ##activities_parks
        cols = ["park_code", "park_name", "park_states", "activity_name"]
        data = []

        response = requests.get(self.api_addresses[0] + self.api_key)
        results = response.json()["data"]

        for item in results:
            for park in item['parks']:
                lst = [self.dc(park['parkCode']), self.dc(park['fullName']), self.dc(park['states']),
                       self.dc(item['name'])]
                data.append(lst)
        # print(data)
        activities_df = pd.DataFrame(data=data, columns=cols)
        # print(activities_df.to_string())

        ##amenities_parks
        cols = ["park_code", "amenity_name", "url"]
        data = []

        response = requests.get(self.api_addresses[1] + self.api_key)
        results = response.json()["data"]

        for item in results:
            for park in item[0]["parks"]:
                for place in park["places"]:
                    lst = [self.dc(park["parkCode"]), self.dc(item[0]["name"]), self.dc(place["url"])]
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
        # print(amenities_vc_df.to_string())

        ##campgrounds
        cols = ["park_code", "paved_roads", "campground_classification", "general_ADA", "wheelchair_access_campground",
                "rv_allowed", "rv_info", "rv_max_length", "trailers_allowed", "trailer_max_length", "description",
                "campground_id",
                "campsite_name", "url", "cell_reception", "camp_store", "dump_station", "internet", "potable_water",
                "showers", "toilets", "campsites_electric", "campsites_group", "campsites_horse", "campsites_other",
                "campsites_rv_only", "campsites_tent_only", "campsites_boat_ramp", "total_sites", "staff_volunteer"]
        data = []

        response = requests.get(self.api_addresses[3] + self.api_key)
        results = response.json()["data"]
        #jprint(results)
        # for item in results:
        #     for park in item[0]["parks"]:
        #         for place in park["places"]:
        #             lst = [self.dc(park["parkCode"]), self.dc(item[0]["name"]), self.dc(place["url"])]
        #             data.append(lst)
        i = 0
        for item in results:
            print(self.dc(item['id']), self.dc(item['name']), self.dc(item['url']))
            # for road in item['accessibility']['accessRoads']:
            #     print(road)
            #     lst += self.dc(item['parkCode']), self.dc(road)
            #
            # for classification in item['accessibility']['classifications']:
            #     lst.append(self.dc(classification))
            # #print(lst)
            # lst += [self.dc(item['accessibility']['adaInfo']),
            #            self.dc(item['accessibility']['wheelchairAccess']),
            #            self.dc(item['accessibility']['rvAllowed']), self.dc(item['accessibility']['rvInfo']),
            #            self.dc(item['accessibility']['rvMaxLength']),
            #            self.dc(item['accessibility']['trailerAllowed']), self.dc(item['accessibility']['trailerMaxLength']),
            #            self.dc(item['description']), self.dc(item['id']), self.dc(item['name']), self.dc(item['url']),
            #            self.dc(item['amenities']['cellPhoneReception']),
            #            self.dc(item['amenities']['campStore']), self.dc(item['amenities']['dumpStation']),
            #            self.dc(item['amenities']['internetConnectivity']),
            #            self.dc(item['amenities']['potableWater']), self.dc(item['amenities']['showers']),
            #            self.dc(item['amenities']['toilets']),
            #            self.dc(item['campsites']['electricalHookups']), self.dc(item['campsites']['group']),
            #            self.dc(item['campsites']['horse']),
            #            self.dc(item['campsites']['other']), self.dc(item['campsites']['rvOnly']),
            #            self.dc(item['campsites']['tentOnly']),
            #            self.dc(item['campsites']['walkBoatTo']), self.dc(item['campsites']['totalSites']),
            #            self.dc(item['amenities']['staffOrVolunteerHostOnsite'])]

            data.append(lst)

        #print(data)
        # campgrounds_df = pd.DataFrame(data=data, columns=cols)
        # print(campgrounds_df.to_string())
        #
        # ##parking_lots
        # cols = ["id", "name", "ADA_facility_description", "is_lot_accessible", "number_oversized_spaces", "number_ADA_spaces",
        #         "number_ADA_Step_Free_Spaces", "number_ADA_van_spaces", "description", "parkCode"]
        # data = []
        #
        # response = requests.get(self.api_addresses[4] + self.api_key)
        # results = response.json()["data"]
        # # jprint(results)
        #
        # for item in results:
        #     lst = [self.dc(item['id']), self.dc(item['name']), self.dc(item['accessibility']['adaFacilitiesDescription']),
        #            self.dc(item['accessibility']['isLotAccessibleToDisabled']), \
        #            self.dc(item['accessibility']['numberOfOversizeVehicleSpaces']), \
        #            self.dc(item['accessibility']['numberofAdaSpaces']), \
        #            self.dc(item['accessibility']['numberofAdaStepFreeSpaces']), \
        #            self.dc(item['accessibility']['numberofAdaVanAccessbileSpaces']), \
        #            self.dc(item['description'])]
        #     for park in item['relatedParks']:
        #         lst.append(self.dc(park['parkCode']))
        #         data.append(lst)
        # #print(data)
        # parking_lot_df = pd.DataFrame(data=data, columns=cols)
        # print(parking_lot_df.to_string())
        #
        # ##places
        # cols = ["id", "title", "url", "park_code"]
        # data = []
        #
        # response = requests.get(self.api_addresses[5] + self.api_key)
        # results = response.json()['data']
        # # jprint(results)
        #
        # i = 0
        # for item in results:
        #     i += 1
        #     lst = [self.dc(item['id']), self.dc(item['title']), self.dc(item['url'])]
        #     multiple = []
        #     for park in item['relatedParks']:
        #         multiple.append(park['parkCode'])
        #     lst.append(self.dc(multiple))
        #
        #     data.append(lst)
        #     print(i)
        # #print(data)
        # places_df = pd.DataFrame(data=data, columns=cols)
        # print(places_df.to_string())