class ParkResults:

    def __init__(self):
        self.results_list = ''

    @classmethod
    def param_constructor(cls, park_info_df, campground_results_df, parking_lot_results_df):
        activity_list = []
        amenity_list = []
        state_list = []
        for i in range(len(park_info_df['park_name'])):
            for park in park_info_df['park_name'][i]:
                print(park)
                for state in park_info_df['park_states'][i]:
                    state_list.append(state)
                print("State(s): ")
                print(*state_list, sep=", ")
                for activity in park_info_df['activity_name'][i]:
                    activity_list.append(activity)
                print("Activities: ")
                print(*activity_list, sep=", ")
                for amenity in park_info_df['amenity_name'][i]:
                    amenity_list.append(amenity)
                print("Amenities: ")
                print(*amenity_list, sep=", ")
                # for campground in campground_results_df['park_code'].isin(park_info_df['park_code'][i]):
                #     print(campground['campground_name'])

        # print(park_info_df.to_string(max_rows=5))
        # print(campground_results_df.to_string(max_rows=5))



    #     for i in range(0, row_count):
    #         cls.campground_name = ', '.join(str(campground_info_df.loc[i, 'campground_name']))
    #         cls.campground_road = ', '.join(str(campground_info_df.loc[i, 'campground_road']))
    #         cls.campground_classification = ', '.join(str(campground_info_df.loc[i, 'campground_classification']))
    #         cls.campground_general_ADA = ', '.join(str(campground_info_df.loc[i, 'campground_general_ADA']))
    #         cls.campground_wheelchair_access = ', '.join(str(campground_info_df.loc[i, 'campground_wheelchair_access']))
    #         cls.campground_rv_info = ', '.join(str(campground_info_df.loc[i, 'campground_rv_info']))
    #         cls.campground_description = ', '.join(str(campground_info_df.loc[i, 'campground_description']))
    #         cls.campground_cell_reception = ', '.join(str(campground_info_df.loc[i, 'campground_cell_reception']))
    #         cls.campground_camp_store = ','.join(str(campground_info_df.loc[i, 'campground_camp_store']))
    #         cls.campground_internet = ', '.join(str(campground_info_df.loc[i, 'campground_internet']))
    #         cls.campground_potable_water = ', '.join(str(campground_info_df.loc[i, 'campground_potable_water']))
    #         cls.campground_toilets = ', '.join(str(campground_info_df.loc[i, 'campground_toilets']))
    #         cls.campground_campsites_electric = ', '.join(str(campground_info_df.loc[i, 'campground_campsites_electric']))
    #         cls.campground_staff_volunteer = ', '.join(str(campground_info_df.loc[i, 'campground_staff_volunteer']))
    #         cls.display_campgrounds(cls)
    #     print(cls.campground_road)
    #
    #     row_count = parking_lot_info_df.shape[0]
    #     for i in range(0, row_count):
    #         cls.parking_lots_name = ', '.join(str(parking_lot_info_df.loc[i, 'parking_lots_name']))
    #         cls.parking_lots_ADA_facility_description = ', '.join(str(parking_lot_info_df.loc[i, 'parking_lots_ADA_facility_description']))
    #         cls.parking_lots_is_lot_accessible = ', '.join(str(parking_lot_info_df.loc[i, 'parking_lots_is_lot_accessible']))
    #         cls.parking_lots_number_oversized_spaces = ', '.join(str(parking_lot_info_df.loc[i, 'parking_lots_number_oversized_spaces']))
    #         cls.parking_lots_number_ADA_spaces = ', '.join(str(parking_lot_info_df.loc[i, 'parking_lots_number_ADA_spaces']))
    #         cls.parking_lots_number_ADA_Step_Free_Spaces = ', '.join(str(parking_lot_info_df.loc[i, 'parking_lots_number_ADA_Step_Free_Spaces']))
    #         cls.parking_lots_number_ADA_van_spaces = ', '.join(str(parking_lot_info_df.loc[i, 'parking_lots_number_ADA_van_spaces']))
    #         cls.parking_lots_description = ', '.join(str(parking_lot_info_df.loc[i, 'parking_lots_description']))
    #         cls.display_parking_lots(cls)
    #     print(cls.parking_lots_number_ADA_spaces)
    #
    #     # return cls.results_list
    #
    # def display_park(cls):
    #     cls.results_list = 'Name: {}  State: {}   Activities: {} \n\nAmenities: {}, \n\nAmenities_URL:' \
    #                        ' {}\n\n'.format(cls.park_name, cls.park_states, cls.park_activities, cls.park_amenities,
    #                                         cls.park_amenities_urls)
    #
    # def display_campgrounds(cls):
    #     cls.results_list += 'Campground Name: {}\nCampground Description: {}\n\n \n\nCampground Roads: {}, ' \
    #              'Campground Classification: {}, Campground General ADA Information: {}, Campground Wheelchair Access: {}, ' \
    #              'Campground RV Information: {} Campground Cell Reception: {}, Campground Camp Store: {}, ' \
    #              'Campground Internet: {}, Campground Potable Water: {}, Campground Toilets: {}, ' \
    #              'Campground Campsites Electric: {}, Campground Staff or Volunteer: {}\n\n'.format(cls.campground_name,
    #                 cls.campground_description, cls.campground_road, cls.campground_classification,
    #                 cls.campground_general_ADA, cls.campground_wheelchair_access, cls.campground_rv_info,
    #                 cls.campground_cell_reception, cls.campground_camp_store, cls.campground_internet,
    #                 cls.campground_potable_water, cls.campground_toilets, cls.campground_campsites_electric,
    #                 cls.campground_staff_volunteer)
    #
    # def display_parking_lots(cls):
    #     cls.results_list += 'Parking Lot Name: {}, Parking Lot Description: {}, Parking Lot ADA Description: {}, ' \
    #                          'Parking Lot Accessibility: {}, Parking Lot Oversized Spaces: {}, Parking Lot ADA Spaces: {}, ' \
    #                          'Parking Lot ADA Step-Free Spaces: {}, Parking Lot ADA Van Spaces: {},\n\n'.format(
    #                                 cls.parking_lots_name, cls.parking_lots_description,
    #                                 cls.parking_lots_ADA_facility_description, cls.parking_lots_is_lot_accessible,
    #                                 cls.parking_lots_number_oversized_spaces, cls.parking_lots_number_ADA_spaces,
    #                                 cls.parking_lots_number_ADA_Step_Free_Spaces, cls.parking_lots_number_ADA_van_spaces)
    # def display_places(cls):
    #     cls.results_list += 'Place Name: {}, Place URL: {}\n\n\n'.format(cls.places_title, cls.places_url)
