import json

import numpy as np
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
                              "https://developer.nps.gov/api/v1/thingstodo?limit=99000"]
        self.activities_df = []
        self.amenities_parks_df = []
        self.amenities_vc_df = []
        self.campgrounds_df = []
        self.parking_lot_df = []
        self.places_df = []
        self.things_to_do_df = []

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
        self.activities_df = pd.DataFrame(data=data, columns=cols)
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
        self.amenities_parks_df = pd.DataFrame(data=data, columns=cols)
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
        self.amenities_vc_df = pd.DataFrame(data=data, columns=cols)
        # print(amenities_vc_df.to_string())

        ##campgrounds
        cols = ["id", "campground_name", "url", "road", "classification", "park_code", "general_ADA",
                "wheelchair_access_campground", "rv_allowed", "rv_info", "rv_max_length", "trailers_allowed",
                "trailer_max_length", "description", "cell_reception", "camp_store", "dump_station", "internet",
                "potable_water", "showers", "toilets", "campsites_electric", "campsites_group", "campsites_horse",
                "campsites_other", "campsites_rv_only", "campsites_tent_only", "campsites_boat_ramp", "total_sites",
                "staff_volunteer"]
        data = []

        response = requests.get(self.api_addresses[3] + self.api_key)
        results = response.json()["data"]
        #jprint(results)

        for item in results:
            lst = [self.dc(item['id']), self.dc(item['name']), self.dc(item['url'])]
            for road in item['accessibility']['accessRoads']:
                lst.append(self.dc(road))
            for classification in item['accessibility']['classifications']:
                lst.append(self.dc(classification))
            lst += [item['parkCode'], self.dc(item['accessibility']['adaInfo']), self.dc(item['accessibility']['wheelchairAccess']),
                    self.dc(item['accessibility']['rvAllowed']), self.dc(item['accessibility']['rvInfo']),
                    self.dc(item['accessibility']['rvMaxLength']), self.dc(item['accessibility']['trailerAllowed']),
                    self.dc(item['accessibility']['trailerMaxLength']), self.dc(item['description']),
                    self.dc(item['amenities']['cellPhoneReception']), self.dc(item['amenities']['campStore']),
                    self.dc(item['amenities']['dumpStation']), self.dc(item['amenities']['internetConnectivity']),
                    self.dc(item['amenities']['potableWater']), self.dc(item['amenities']['showers']),
                    self.dc(item['amenities']['toilets']), self.dc(item['campsites']['electricalHookups']),
                    self.dc(item['campsites']['group']), self.dc(item['campsites']['horse']),
                    self.dc(item['campsites']['other']), self.dc(item['campsites']['rvOnly']),
                    self.dc(item['campsites']['tentOnly']), self.dc(item['campsites']['walkBoatTo']),
                    self.dc(item['campsites']['totalSites']), self.dc(item['amenities']['staffOrVolunteerHostOnsite'])]

            data.append(lst)

        #print(data)
        self.campgrounds_df = pd.DataFrame(data=data, columns=cols)
        #print(campgrounds_df.to_string())

        ##parking_lots
        cols = ["id", "name", "ADA_facility_description", "is_lot_accessible", "number_oversized_spaces", "number_ADA_spaces",
                "number_ADA_Step_Free_Spaces", "number_ADA_van_spaces", "description", "parkCode"]
        data = []

        response = requests.get(self.api_addresses[4] + self.api_key)
        results = response.json()["data"]
        # jprint(results)

        for item in results:
            lst = [self.dc(item['id']), self.dc(item['name']), self.dc(item['accessibility']['adaFacilitiesDescription']),
                   self.dc(item['accessibility']['isLotAccessibleToDisabled']),
                   self.dc(item['accessibility']['numberOfOversizeVehicleSpaces']),
                   self.dc(item['accessibility']['numberofAdaSpaces']),
                   self.dc(item['accessibility']['numberofAdaStepFreeSpaces']),
                   self.dc(item['accessibility']['numberofAdaVanAccessbileSpaces']),
                   self.dc(item['description'])]
            for park in item['relatedParks']:
                lst.append(self.dc(park['parkCode']))
                data.append(lst)
        #print(data)
        self.parking_lot_df = pd.DataFrame(data=data, columns=cols)
        # print(parking_lot_df.to_string())

        ##places
        cols = ["id", "title", "url", "park_code"]
        data = []

        response = requests.get(self.api_addresses[5] + self.api_key)
        results = response.json()['data']
        # jprint(results)

        for item in results:
            lst = [self.dc(item['id']), self.dc(item['title']), self.dc(item['url'])]
            multiple = []
            for park in item['relatedParks']:
                multiple.append(park['parkCode'])
            lst.append(self.dc(multiple))

            data.append(lst)

        #print(data)
        self.places_df = pd.DataFrame(data=data, columns=cols)
        # print(places_df.to_string())

        ##things to do
        cols = ["id", "activity_name", "accessibility_information", "location", "title", "url", "park_code", "topic_name"]
        data = []

        response = requests.get(self.api_addresses[6] + self.api_key)
        results = response.json()['data']
        # jprint(results)

        for item in results:
            for names in item['activities']:
                lst = [self.dc(item['id']), self.dc(names['name']), self.dc(item['accessibilityInformation']),
                       self.dc(item['location']), self.dc(item['title']), self.dc(item['url'])]

            multiple = []
            for park in item['relatedParks']:
                multiple.append(park['parkCode'])
            lst.append(self.dc(multiple))
            multiple.clear()

            for topic in item['topics']:
                multiple = (topic['name'])
            # print(multiple)
            lst.append(self.dc(multiple))

            data.append(lst)

        # print(list)
        self.things_to_do_df = pd.DataFrame(data=data, columns=cols)
        #print(things_to_do_df.to_string())

    def fetch_dropdown_list_data(self):
        distinct_activities_parks = []
        distinct_amenities = []
        distinct_parks = []
        distinct_states = []
        length_to_find = 2
        try:
            distinct_activities_parks = self.activities_df["activity_name"].unique()
            distinct_amenities = self.amenities_parks_df["amenity_name"].unique()
            distinct_parks = self.activities_df["park_name"].unique()
            distinct_states = self.activities_df.loc[self.activities_df["park_states"].str.len() == length_to_find,"park_states"].unique()
            # states_list = self.activities_df["park_states"].unique()
            # for state in states_list:
            #     if len(state) == 2:
            #         distinct_states.append(state)

        except ConnectionError:
            print("4: An error occurred; please try again.")

        return distinct_activities_parks, distinct_amenities, distinct_parks, distinct_states

    def fetch_results(self, activities_selection, amenities_selection, states_selection, parks_selection):
        park_list = []
        #self.results_df = pd.DataFrame(data=data, columns=cols)

        try:
            undup_activities = self.activities_df.drop_duplicates(subset=['park_name', 'activity_name'])
            pandas_select = pd.merge(undup_activities, self.amenities_parks_df, on='park_code', how='left')
            #print(pandas_select.to_string())

            if activities_selection and amenities_selection and parks_selection and states_selection:
                boo = pandas_select[pandas_select["activity_name"].isin(activities_selection)] & \
                pandas_select[pandas_select["amenity_name"].isin(amenities_selection)] & \
                pandas_select[pandas_select["park_states"].isin(activities_selection)] & \
                pandas_select[pandas_select["park_name"].isin(activities_selection)]
            print(boo.to_string())


        #
        #     if activities_selection:
        #         where_logic = " activity_name IN ("                                      # df[df['col_1'].isin([1,2,3])]
        #         if len(activities_selection) > 1:                         df[(df['col_1'] == 11) & (df['col_2'] > 5)]
        #             for activity in activities_selection[:-1]:
        #                 where_logic += "'" + activity + "'" + ','
        #         where_logic += "'" + activities_selection[-1] + "') "
        #
        #         if amenities_selection or states_selection or parks_selection:
        #             where_logic += "and"
        #
        #     if amenities_selection:
        #         where_logic += " amenity in ("
        #         if len(amenities_selection) > 1:
        #             for amenity in amenities_selection[:-1]:
        #                 where_logic += "'" + amenity + "'" + ','
        #         where_logic += "'" + amenities_selection[-1] + "') "
        #         print(where_logic)
        #
        #         if states_selection or parks_selection:
        #             where_logic += "and"
        #             print(where_logic)
        #
        #     if states_selection:
        #         where_logic += " park_states in ("
        #         if len(states_selection) > 1:
        #             for state in states_selection[:-1]:
        #                 where_logic += "'" + state + "'" + ','
        #         where_logic += "'" + states_selection[-1] + "') "
        #
        #         if parks_selection:
        #             where_logic += "and"
        #
        #     if parks_selection:
        #         where_logic += " park_name in ("
        #         if len(parks_selection) > 1:
        #             for park in parks_selection[:-1]:
        #                 where_logic += "'" + park + "'" + ','
        #         where_logic += "'" + parks_selection[-1] + "') "
        #
        #     select_statement += where_logic + "ORDER BY park_name"
        #     print(select_statement)
        #     __cursor.execute(select_statement)
        #
        #     for park_name in list(__cursor):
        #         # park_list += park_name
        #         park_state = "foo"
        #         park_information = "boo"
        #         park_list.append(ParkResults(park_name[0], park_state, park_information))
        #     print("A")
        #
        #     # for park in park_list:
        #     #     print('Name: {},   State: {},   Information: {}'.format(park.park_name, park.park_state, park.park_information))
        #
        #     # ParkResults.display_park(park_list)
        #     # ParkResults.save_to_file(park_list)
        except ConnectionError:
            print("4: Connection interrupted; please try again.")
        # finally:
        #     __cursor.close()
        #
        # return park_list
        #
