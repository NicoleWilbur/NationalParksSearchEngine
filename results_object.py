class ParkResults:

    def __init__(self, results_df):
        park_info_dictionary = results_df.groupby('park_name').agg(
            {'park_name': set, 'park_states': set, 'activity_name': set, 'amenity_name': set, 'amenity_url': set}).to_dict()
        # print(park_info_dictionary)
        campground_info_dictionary = results_df.groupby('park_name').agg(
            {'campground_name': set, 'campground_url': set, 'campground_road': set, 'campground_classification': set,
             'campground_general_ADA': set, 'campground_wheelchair_access': set, 'campground_rv_info': set,
             'campground_description': set, 'campground_cell_reception': set, 'campground_camp_store': set,
             'campground_internet': set, 'campground_potable_water': set, 'campground_toilets': set,
             'campground_campsites_electric': set, 'campground_staff_volunteer': set}).to_dict()
        # print(campground_info_dictionary)
        places_info_dictionary = results_df.groupby('park_name').agg(
            {'places_title': set, 'places_url': set}).to_string()
        # print(places_info_dictionary)
        parking_lot_info_dictionary = results_df.groupby('park_name').agg(
            {'parking_lots_name': set, 'parking_lots_ADA_facility_description': set,
             'parking_lots_is_lot_accessible': set, 'parking_lots_number_oversized_spaces': set,
             'parking_lots_number_ADA_spaces': set, 'parking_lots_number_ADA_Step_Free_Spaces': set,
             'parking_lots_number_ADA_van_spaces': set, 'parking_lots_description': set}).to_dict()
        # print(parking_lot_info_dictionary)

        self.park_name = park_info_dictionary['park_name'][0]
        self.park_state = park_info_dictionary['park_states']
        self.park_activities = park_info_dictionary['activity_name']
        self.park_amenities = park_info_dictionary['amenity_name']
        self.park_amenities_urls = park_info_dictionary['amenity_url']
        self.park_campground_name = campground_info_dictionary['campground_name']
        #
        # self.park_information = park_information
        # self.park_url = park_url
        # self.park_phone_number = park_phone_number
        # self.park_tty_number = park_tty_number
        # self.park_email_address = park_email_address

    def display_park(self):
        print(self.park_name, self.park_state, self.park_activities, self.park_amenities, self.park_amenities_urls,
              self.park_campground_name)
        #print('Name: {},   State: {},   Information: {}'.format(park.park_name, park.park_state, park.park_information))
        # return self.park_name + ", " + self.park_state + ", " + self.park_activities + ", " + self.park_amenities + ", " + \
        #        self.park_amenities_urls + ", " + self.park_campground_name
