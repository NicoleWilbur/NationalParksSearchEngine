from tkinter import messagebox

import requests
import pandas as pd

from park_results import ParkResults


class APIPandas:

    def __init__(self, api_key):
        self.api_key = api_key
        self.api_addresses = ['https://developer.nps.gov/api/v1/activities/parks?limit=99000',
                              'https://developer.nps.gov/api/v1/amenities/parksplaces?limit=99000',
                              'https://developer.nps.gov/api/v1/campgrounds?limit=99000?',
                              'https://developer.nps.gov/api/v1/parkinglots?limit=99000']
        self.activities_df = []
        self.amenities_parks_df = []
        self.campgrounds_df = []
        self.parking_lot_df = []
        self.parks_df = []
        self.states_df = []

    @staticmethod
    def dc(data):
        string = ''
        if not data:
            scrubbed = 'No Data'
        elif isinstance(data, list):
            for i in data:
                string += i + ' & '
            scrubbed = string[:-2]
        else:
            scrubbed = data
        return scrubbed

    def get_api_data(self):

        ##activities_parks
        cols = ['park_code', 'park_name', 'park_states', 'activity_name']
        data = []

        response = requests.get(self.api_addresses[0] + self.api_key)
        results = response.json()['data']

        for item in results:
            for park in item['parks']:
                lst = [self.dc(park['parkCode']), self.dc(park['fullName']), self.dc(park['states']),
                       self.dc(item['name'])]
                data.append(lst)
        self.activities_df = pd.DataFrame(data=data, columns=cols)

        ##amenities_parks
        cols = ['park_code', 'amenity_name', 'amenity_url']
        data = []

        response = requests.get(self.api_addresses[1] + self.api_key)
        results = response.json()['data']

        for item in results:
            for park in item[0]['parks']:
                for place in park['places']:
                    lst = [self.dc(park['parkCode']), self.dc(item[0]['name']), self.dc(place['url'])]
                    data.append(lst)
        self.amenities_parks_df = pd.DataFrame(data=data, columns=cols)

        ##campgrounds
        cols = ['park_code', 'campground_id', 'campground_name', 'campground_url', 'campground_road',
                'campground_classification', 'campground_general_ADA', 'campground_wheelchair_access',
                'campground_rv_allowed', 'campground_rv_info', 'campground_rv_max_length',
                'campground_trailers_allowed',
                'campground_trailer_max_length', 'campground_description', 'campground_cell_reception',
                'campground_camp_store', 'campground_dump_station', 'campground_internet', 'campground_potable_water',
                'campground_showers', 'campground_toilets', 'campground_campsites_electric',
                'campground_campsites_group',
                'campground_campsites_horse', 'campground_campsites_other', 'campground_campsites_rv_only',
                'campground_campsites_tent_only', 'campground_campsites_boat_ramp', 'campground_total_sites',
                'campground_staff_volunteer']
        data = []

        response = requests.get(self.api_addresses[2] + self.api_key)
        results = response.json()['data']


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

        self.campgrounds_df = pd.DataFrame(data=data, columns=cols)

        ##parking_lots
        cols = ['parking_lots_id', 'parking_lots_name', 'parking_lots_ADA_facility_description',
                'parking_lots_is_lot_accessible', 'parking_lots_number_oversized_spaces',
                'parking_lots_number_ADA_spaces',
                'parking_lots_number_ADA_Step_Free_Spaces', 'parking_lots_number_ADA_van_spaces',
                'parking_lots_description', 'park_code']
        data = []

        response = requests.get(self.api_addresses[3] + self.api_key)
        results = response.json()['data']

        for item in results:
            lst = [self.dc(item['id']), self.dc(item['name']),
                   self.dc(item['accessibility']['adaFacilitiesDescription']),
                   self.dc(item['accessibility']['isLotAccessibleToDisabled']),
                   self.dc(item['accessibility']['numberOfOversizeVehicleSpaces']),
                   self.dc(item['accessibility']['numberofAdaSpaces']),
                   self.dc(item['accessibility']['numberofAdaStepFreeSpaces']),
                   self.dc(item['accessibility']['numberofAdaVanAccessbileSpaces']),
                   self.dc(item['description'])]
            for park in item['relatedParks']:
                lst.append(self.dc(park['parkCode']))
                data.append(lst)

        self.parking_lot_df = pd.DataFrame(data=data, columns=cols)

    def fetch_dropdown_list_data(self):
        length_to_find = 2

        distinct_activities_parks = self.activities_df['activity_name'].unique().tolist()
        distinct_amenities = self.amenities_parks_df['amenity_name'].unique().tolist()
        distinct_parks = self.activities_df['park_name'].unique().tolist()
        distinct_states = self.activities_df.loc[
            self.activities_df['park_states'].str.len() == length_to_find, 'park_states'].unique().tolist()

        return distinct_activities_parks, distinct_amenities, distinct_parks, distinct_states

    def fetch_results(self, activities_selection = [], amenities_selection = [], parks_selection = [], states_selection = []):
        if activities_selection:
            activities_selection_df = self.activities_df['park_code'][self.activities_df['activity_name'].
                                        isin(activities_selection)].drop_duplicates()
        else:
            activities_selection_df = pd.DataFrame()
        if amenities_selection:
            amenities_selection_df = self.amenities_parks_df['park_code'][self.amenities_parks_df['amenity_name'].
                                        isin(amenities_selection)].drop_duplicates()
        else:
            amenities_selection_df = pd.DataFrame()
        if states_selection:
            states_selection_df = self.activities_df['park_code'][self.activities_df['park_states'].
                                        isin(states_selection)].drop_duplicates()
        else:
            states_selection_df = pd.DataFrame()
        if parks_selection:
            parks_selection_df = self.activities_df['park_code'][self.activities_df['park_name'].
                                        isin(parks_selection)].drop_duplicates()
        else:
            parks_selection_df = pd.DataFrame()

        pandas_select_df = pd.DataFrame(columns=['Park Code'], index=range(1,))

        if not activities_selection_df.empty and not amenities_selection_df.empty and not parks_selection_df.empty \
                and not states_selection_df.empty:
            pandas_select_df = activities_selection_df[activities_selection_df.isin(amenities_selection_df) &
                                           activities_selection_df.isin(states_selection_df) & activities_selection_df.
                                           isin(parks_selection_df)].drop_duplicates()
        elif not activities_selection_df.empty and not amenities_selection_df.empty and not states_selection_df.empty \
                and parks_selection_df.empty:
            pandas_select_df = activities_selection_df[activities_selection_df.isin(amenities_selection_df) &
                                           activities_selection_df.isin(states_selection_df)].drop_duplicates()
        elif not activities_selection_df.empty and not amenities_selection_df.empty and parks_selection_df.empty \
                and states_selection_df.empty:
            pandas_select_df = activities_selection_df[activities_selection_df.isin(amenities_selection_df)].drop_duplicates()
        elif not activities_selection_df.empty and amenities_selection_df.empty and not parks_selection_df.empty\
                and not states_selection_df.empty:
            pandas_select_df = activities_selection_df[activities_selection_df.isin(states_selection_df) & activities_selection_df.
                                           isin(parks_selection_df)].drop_duplicates()
        elif not activities_selection_df.empty and amenities_selection_df.empty and not parks_selection_df.empty and \
                states_selection_df.empty:
            pandas_select_df = activities_selection_df[activities_selection_df.isin(parks_selection_df)].drop_duplicates()
        elif not activities_selection_df.empty and amenities_selection_df.empty and parks_selection_df.empty and \
                not states_selection_df.empty:
            pandas_select_df = activities_selection_df[activities_selection_df.isin(states_selection_df)].drop_duplicates()
        elif not activities_selection_df.empty and not amenities_selection_df.empty and not parks_selection_df.empty \
                and states_selection_df.empty:
            pandas_select_df = activities_selection_df[activities_selection_df.isin(amenities_selection_df) & activities_selection_df.
                                           isin(parks_selection_df)].drop_duplicates()
        elif not activities_selection_df.empty and amenities_selection_df.empty and parks_selection_df.empty and \
                states_selection_df.empty:
            pandas_select_df = activities_selection_df.drop_duplicates()
        elif activities_selection_df.empty and not amenities_selection_df.empty and not parks_selection_df.empty\
                and not states_selection_df.empty:
            pandas_select_df = amenities_selection_df[amenities_selection_df.isin(states_selection_df) & amenities_selection_df.
                                           isin(parks_selection_df)].drop_duplicates()
        elif activities_selection_df.empty and not amenities_selection_df.empty and parks_selection_df.empty and \
                not states_selection_df.empty:
            pandas_select_df = amenities_selection_df[amenities_selection_df.isin(states_selection_df)].drop_duplicates()
        elif activities_selection_df.empty and not amenities_selection_df.empty and not parks_selection_df.empty\
                and states_selection_df.empty:
            pandas_select_df = amenities_selection_df[amenities_selection_df.isin(parks_selection_df)].drop_duplicates()
        elif activities_selection_df.empty and not amenities_selection_df.empty and parks_selection_df.empty and \
                states_selection_df.empty:
            pandas_select_df = amenities_selection_df.drop_duplicates()
        elif activities_selection_df.empty and amenities_selection_df.empty and not parks_selection_df.empty and \
                not states_selection_df.empty:
            pandas_select_df = parks_selection_df[parks_selection_df.isin(states_selection_df)].drop_duplicates()
        elif activities_selection_df.empty and amenities_selection_df.empty and not parks_selection_df.empty and \
                states_selection_df.empty:
            pandas_select_df = parks_selection_df.drop_duplicates()
        elif activities_selection_df.empty and amenities_selection_df.empty and parks_selection_df.empty and \
                not states_selection_df.empty:
            pandas_select_df = states_selection_df.drop_duplicates()
        else:
            messagebox.showerror('Yikes! Something went wrong. Please try another selection.')

        results_df = pd.merge(pandas_select_df, self.activities_df, on='park_code', how='left')

        park_results_df = pd.merge(results_df, self.amenities_parks_df[['park_code', 'amenity_name', 'amenity_url']]
                                                                , on='park_code', how='left')
        park_results_df.fillna("No Data", inplace=True)

        park_info_df = pd.DataFrame(park_results_df.groupby('park_code').agg(
            {'park_code': set, 'park_name': set, 'park_states': set, 'activity_name': set,
             'amenity_name': set, 'amenity_url': set}))
        park_info_df.index = range(len(park_info_df))

        campground_results_df = pd.merge(pandas_select_df, self.campgrounds_df[['park_code', 'campground_name',
                                                                'campground_road', 'campground_classification',
                                                               'campground_general_ADA',
                                                               'campground_wheelchair_access',
                                                               'campground_rv_info', 'campground_description',
                                                               'campground_cell_reception', 'campground_camp_store',
                                                               'campground_internet', 'campground_potable_water',
                                                               'campground_toilets',
                                                               'campground_campsites_electric',
                                                               'campground_staff_volunteer']], on='park_code',
                                                                how='left').drop_duplicates()

        parking_lots_results_df = pd.merge(pandas_select_df, self.parking_lot_df[['park_code', 'parking_lots_name',
                                                                'parking_lots_ADA_facility_description',
                                                                'parking_lots_is_lot_accessible', 'parking_lots_number_oversized_spaces',
                                                                'parking_lots_number_ADA_spaces',
                                                                'parking_lots_number_ADA_Step_Free_Spaces',
                                                                'parking_lots_number_ADA_van_spaces',
                                                                'parking_lots_description']], on='park_code',
                                                                how='left').drop_duplicates()

        return park_info_df, campground_results_df, parking_lots_results_df
