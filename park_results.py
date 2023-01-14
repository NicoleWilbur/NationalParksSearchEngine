class ParkResults:

    def __init__(self, park_info_df, campground_info_df, places_info_df, parking_lot_info_df):

        row_count = park_info_df.shape[0]
        for i in range(0, row_count):
            self.park_name = ', '.join(park_info_df.loc[i, 'park_name'])
            self.park_states = ', '.join(park_info_df.loc[i, 'park_states'])
            self.park_activities = ', '.join(park_info_df.loc[i, 'activity_name'])
            self.park_amenities = ', '.join(park_info_df.loc[i, 'amenity_name'])
            self.park_amenities_urls = ', '.join(park_info_df.loc[i, 'amenity_url'])
            self.display_park()

        row_count = campground_info_df.shape[0]
        for i in range(0, row_count):
            self.campground_name = ', '.join(campground_info_df.loc[i, 'campground_name'])
            self.campground_url = ', '.join(campground_info_df.loc[i, 'campground_url'])
            self.campground_road = ', '.join(campground_info_df.loc[i, 'campground_road'])
            self.campground_classification = ', '.join(campground_info_df.loc[i, 'campground_classification'])
            self.campground_general_ADA = ', '.join(campground_info_df.loc[i, 'campground_general_ADA'])
            self.campground_wheelchair_access = ', '.join(campground_info_df.loc[i, 'campground_wheelchair_access'])
            self.campground_rv_info = ', '.join(campground_info_df.loc[i, 'campground_rv_info'])
            self.campground_description = ', '.join(campground_info_df.loc[i, 'campground_description'])
            self.campground_cell_reception = ', '.join(campground_info_df.loc[i, 'campground_cell_reception'])
            self.campground_camp_store = ','.join(campground_info_df.loc[i, 'campground_camp_store'])
            self.campground_internet = ', '.join(campground_info_df.loc[i, 'campground_internet'])
            self.campground_potable_water = ', '.join(campground_info_df.loc[i, 'campground_potable_water'])
            self.campground_toilets = ', '.join(campground_info_df.loc[i, 'campground_toilets'])
            self.campground_campsites_electric = ', '.join(campground_info_df.loc[i, 'campground_campsites_electric'])
            self.campground_staff_volunteer = ', '.join(campground_info_df.loc[i, 'campground_staff_volunteer'])
            self.display_campgrounds()

        row_count = parking_lot_info_df.shape[0]
        for i in range(0, row_count):
            self.parking_lots_name = ', '.join(parking_lot_info_df.loc[i, 'parking_lots_name'])
            self.parking_lots_ADA_facility_description = ', '.join(parking_lot_info_df.loc[i, 'parking_lots_ADA_facility_description'])
            self.parking_lots_is_lot_accessible = ', '.join(str(parking_lot_info_df.loc[i, 'parking_lots_is_lot_accessible']))
            self.parking_lots_number_oversized_spaces = ', '.join(str(parking_lot_info_df.loc[i, 'parking_lots_number_oversized_spaces']))
            self.parking_lots_number_ADA_spaces = ', '.join(str(parking_lot_info_df.loc[i, 'parking_lots_number_ADA_spaces']))
            self.parking_lots_number_ADA_Step_Free_Spaces = ', '.join(str(parking_lot_info_df.loc[i, 'parking_lots_number_ADA_Step_Free_Spaces']))
            self.parking_lots_number_ADA_van_spaces = ', '.join(str(parking_lot_info_df.loc[i, 'parking_lots_number_ADA_van_spaces']))
            self.parking_lots_description = ', '.join(parking_lot_info_df.loc[i, 'parking_lots_description'])
            self.display_parking_lots()

        row_count = places_info_df.shape[0]
        for i in range(0, row_count):
            self.places_title = ', '.join(places_info_df.loc[i, 'places_title'])
            self.places_url = ', '.join(places_info_df.loc[i, 'places_url'])
            self.display_places()

        # self.park_information = park_information
        # self.park_url = park_url
        # self.park_phone_number = park_phone_number
        # self.park_tty_number = park_tty_number
        # self.park_email_address = park_email_address

    def display_park(self):
        print('Name: {}, State: {}, Activities: {}, Amenities: {}, Amenities_URL: {}'.format(self.park_name,
                self.park_states, self.park_activities, self.park_amenities, self.park_amenities_urls))

    def display_campgrounds(self):
        print('Campground Name: {}, Campground Description: {}, Campground URLs: {}, Campground Roads: {}, Campground Classification: {}, '
            'Campground General ADA Information: {}, Campground Wheelchair Access: {}, Campground RV Information: {}'
            'Campground Cell Reception: {}, Campground Camp Store: {}, Campground Internet: {}, '
            'Campground Potable Water: {}, Campground Toilets: {}, Campground Campsites Electric: {}, '
            'Campground Staff or Volunteer: {}'.format(self.campground_name, self.campground_description,
                self.campground_url, self.campground_road, self.campground_classification, self.campground_general_ADA,
                self.campground_wheelchair_access, self.campground_rv_info, self.campground_cell_reception,
                self.campground_camp_store, self.campground_internet, self.campground_potable_water,
                self.campground_toilets, self.campground_campsites_electric, self.campground_staff_volunteer))

    def display_parking_lots(self):
        print('Parking Lot Name: {}, Parking Lot Description: {}, Parking Lot ADA Description: {}, Parking Lot Accessibility: {}, '
              'Parking Lot Oversized Spaces: {}, Parking Lot ADA Spaces: {}, Parking Lot ADA Step-Free Spaces: {}, '
              'Parking Lot ADA Van Spaces: {},'.format(self.parking_lots_name, self.parking_lots_description,
                self.parking_lots_ADA_facility_description, self.parking_lots_is_lot_accessible,
                self.parking_lots_number_oversized_spaces, self.parking_lots_number_ADA_spaces,
                self.parking_lots_number_ADA_Step_Free_Spaces, self.parking_lots_number_ADA_van_spaces))
    def display_places(self):
        print('Place Name: {}, Place URL: {}'.format(self.places_title, self.places_url))
