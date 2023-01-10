class ParkResults:

    def __init__(self, results_df):
        park_info_dictionary = results_df.groupby('park_name').agg({'park_states': set, 'activity_name': set,
                                                                    'amenity_name': set, 'amenity_url': set,
                                                                    'campground_name': set}).to_string()
        campground_info_dictionary = results_df.groupby('campground_name').agg({'campground_url': set,
                                                                                'campground_road': set,
                                                                                'campground_classification': set,
                                                                                'campground_general_ADA': set,
                                                                                'campground_wheelchair_access': set,
                                                                                'campground_rv_info': set,
                                                                                'campground_description': set,
                                                                                'campground_cell_reception': set,
                                                                                'campground_camp_store': set,
                                                                                'campground_internet': set,
                                                                                'campground_potable_water': set,
                                                                                'campground_toilets': set,
                                                                                'campground_campsites_electric': set,
                                                                                'campground_staff_volunteer': set}).to_string()
        places_info_dictionary = results_df.groupby('places_title').agg({'places_url': set}).to_string()
        parking_lot_info_dictionary = results_df.groupby('parking_lots_name').agg(
            {'parking_lots_ADA_facility_description': set,
             'parking_lots_is_lot_accessible': set, 'parking_lots_number_oversized_spaces': set,
             'parking_lots_number_ADA_spaces': set, 'parking_lots_number_ADA_Step_Free_Spaces': set,
             'parking_lots_number_ADA_van_spaces': set, 'parking_lots_description': set}).to_string()

        self.park_name = park_name
        self.park_state = park_state
        self.park_activities = park_activities
        self.park_amenities = park_amenities
        self.park_amenities_urls = park_amenities_urls
        self.park_campground_name = park_campground_name

        self.park_information = park_information
        self.park_url = park_url
        self.park_phone_number = park_phone_number
        self.park_tty_number = park_tty_number
        self.park_email_address = park_email_address

    def park_basics (self, results_dictionary):
        pass
        # self.park_name = park_name
        # self.park_state = park_state
        # self.park_activities = park_activities
        # self.park_amenities = park_amenities
        # self.park_amenities_urls = park_amenities_urls
        # self.park_campground_name = park_campground_name

    def campground_info (self):
        pass

    def display_park(self):
        print(self.park_name, self.park_state, self.park_information, self.park_url, self.park_phone_number,
              self.park_tty_number, self.park_email_address)
        return self.park_name + ", " + self.park_state + ", " + self.park_information + ", " + self.park_url + ", " + \
               self.park_phone_number + ", " + self.park_tty_number + ", " + self.park_email_address
