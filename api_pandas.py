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
        self.campgrounds_df = []
        self.parking_lot_df = []
        self.places_df = []
        self.things_to_do_df = []
        self.parks_df = []
        self.states_df = []

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
        self.activities_df = pd.DataFrame(data=data, columns=cols)

        ##amenities_parks
        cols = ["park_code", "amenity_name", "amenity_url"]
        data = []

        response = requests.get(self.api_addresses[1] + self.api_key)
        results = response.json()["data"]

        for item in results:
            for park in item[0]["parks"]:
                for place in park["places"]:
                    lst = [self.dc(park["parkCode"]), self.dc(item[0]["name"]), self.dc(place["url"])]
                    data.append(lst)
        self.amenities_parks_df = pd.DataFrame(data=data, columns=cols)

        ##campgrounds
        cols = ["park_code", "campground_id", "campground_name", "campground_url", "campground_road",
                "campground_classification", "campground_general_ADA", "campground_wheelchair_access",
                "campground_rv_allowed", "campground_rv_info", "campground_rv_max_length", "campground_trailers_allowed",
                "campground_trailer_max_length", "campground_description", "campground_cell_reception",
                "campground_camp_store", "campground_dump_station", "campground_internet", "campground_potable_water",
                "campground_showers", "campground_toilets", "campground_campsites_electric", "campground_campsites_group",
                "campground_campsites_horse", "campground_campsites_other", "campground_campsites_rv_only",
                "campground_campsites_tent_only", "campground_campsites_boat_ramp", "campground_total_sites",
                "campground_staff_volunteer"]
        data = []

        response = requests.get(self.api_addresses[3] + self.api_key)
        results = response.json()["data"]
        #jprint(results)

        for item in results:
            lst = [item['parkCode'], self.dc(item['id']), self.dc(item['name']), self.dc(item['url'])]
            for road in item['accessibility']['accessRoads']:
                lst.append(self.dc(road))
            for classification in item['accessibility']['classifications']:
                lst.append(self.dc(classification))
            lst += [self.dc(item['accessibility']['adaInfo']), self.dc(item['accessibility']['wheelchairAccess']),
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
        cols = ["parking_lots_id", "parking_lots_name", "parking_lots_ADA_facility_description",
                "parking_lots_is_lot_accessible", "parking_lots_number_oversized_spaces", "parking_lots_number_ADA_spaces",
                "parking_lots_number_ADA_Step_Free_Spaces", "parking_lots_number_ADA_van_spaces", "parking_lots_description", "park_code"]
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
        #self.parking_lot_df = self.parking_lot_df[-1:] + self.parking_lot_df[:-1]
        # print(parking_lot_df.to_string())

        ##places
        cols = ["park_code", "places_id", "places_title", "places_url"]
        data = []

        response = requests.get(self.api_addresses[5] + self.api_key)
        results = response.json()['data']
        # jprint(results)

        for item in results:
            for park in item['relatedParks']:
                lst = []
                multiple = []
                for park in item['relatedParks']:
                    multiple.append(park['parkCode'])
                lst.append(self.dc(park['parkCode']))
                lst += [self.dc(item['id']), self.dc(item['title']), self.dc(item['url'])]

            data.append(lst)

        # print(data)
        self.places_df = pd.DataFrame(data=data, columns=cols)
        #print(self.places_df.to_string())

        # for item in results:
        #     multiple = []
        #     list = []
        #     for park in item['relatedParks']:
        #         multiple.append(park['parkCode'])
        #     lst.append(self.dc(multiple))
        #     lst += [self.dc(item['id']), self.dc(item['title']), self.dc(item['url'])]
        #     data.append(lst)
        #
        # #print(data)
        # self.places_df = pd.DataFrame(data=data, columns=cols)
        # print(self.places_df.to_string())

        ##things to do
        cols = ["park_code", "things to do_id", "things to do_activity_name", "things to do_accessibility_information",
                "things to do_location", "things to do_title", "things to do_url", "things to do_topic_name"]
        data = []

        response = requests.get(self.api_addresses[6] + self.api_key)
        results = response.json()['data']
        # jprint(results)

        for park in item['relatedParks']:
            lst.append(park['parkCode'])
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
        #print(things_to_do_df.to_string(max_rows))

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

    def fetch_results(self, activities_selection, amenities_selection, parks_selection, states_selection):
        park_list = []
        pandas_where = ""
        pandas_select_df = pd.DataFrame()
        #self.results_df = pd.DataFrame(data=data, columns=cols)
        #print(activities_selection)
        #print(self.activities_df.to_string())
        try:
            activities_selection_df = self.activities_df['park_code'][self.activities_df['activity_name'].isin(activities_selection)].drop_duplicates()
            amenities_selection_df = self.amenities_parks_df['park_code'][self.amenities_parks_df['amenity_name'].isin(amenities_selection)].drop_duplicates()
            states_selection_df = self.activities_df['park_code'][self.activities_df['park_states'].isin(states_selection)].drop_duplicates()
            parks_selection_df = self.activities_df['park_code'][self.activities_df['park_name'].isin(parks_selection)].drop_duplicates()
            print(parks_selection_df.to_string())
            #pd.concat([df1, df2]).drop_duplicates()
            # pandas_select_df = pd.concat([activities_selection_df, amenities_selection_df, states_selection_df], parks_selection_df).drop_duplicates() #--or logic
            # pandas_select_df = activities_selection_df[activities_selection_df.isin(amenities_selection_df) & activities_selection_df.isin(states_selection_df) & activities_selection_df.isin(parks_selection)]
            # print(undup_activities.to_string()
            #pandas_select_df = pd.merge(activities_selection_df, amenities_selection_df, on='park_code', how='left')
            # print(pandas_select_df.to_string())
            # del self.campgrounds_df
            # pandas_select_df = pd.merge(pandas_select_df, self.parking_lot_df, on='park_code', how='left')
            # del self.parking_lot_df
            # pandas_select_df = pd.merge(pandas_select_df, self.places_df, on='park_code', how='left')
            # del self.places_df
            # pandas_select_df = pd.merge(pandas_select_df, self.things_to_do_df, on='park_code', how='left')
            # del self.things_to_do_df

            # if activities_selection:
            #     pandas_select_df = join_amenities + '[join_amenities["activity_name"].isin(activities_selection)]'
            #     if amenities_selection or states_selection or parks_selection:
            #         pandas_where += " & "
            #
            # if activities_selection:
            #     pandas_where += join_amenities + '[join_amenities["amenity_name"].isin(amenities_selection)]'
            #     if states_selection or parks_selection:
            #         pandas_where += " & "
            #
            # if states_selection:
            #     pandas_where += join_amenities + '[join_amenities["park_states"].isin(activities_selection)]'
            #     if parks_selection:
            #         pandas_where += " & "
            #
            # if parks_selection:
            #     pandas_where += join_amenities +'[join_amenities["park_name"].isin(activities_selection)]'
            #     print(pandas_where)

            ##fix below
            #pandas_select_df = pd.merge(undup_activities, self.amenities_parks_df, on='park_code', how='left')

            #print(pandas_select_df.to_string())

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
