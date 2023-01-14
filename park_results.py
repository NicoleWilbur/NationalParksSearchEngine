class ParkResults:

    def __init__(self, park_info_df, campground_results_df, places_info, parking_lot_info):
        # 'park_name': set, 'park_states': set, 'activity_name': set,
        # 'amenity_name': set, 'amenity_url': set})
        print(park_info_df)
        row_count = park_info_df.shape[0]
        print(row_count)
        i = 0
        for i in range(0, row_count):
            self.park_name = park_info_df.loc[i, 'park_name']
            self.park_states = park_info_df.loc[i, 'park_states']
            self.park_activities = park_info_df.loc[i, 'activity_name']
            self.park_amenities = park_info_df.loc[i, 'amenity_name']
            self.park_amenities_urls = park_info_df.loc[i, 'amenity_url']

        print(self.park_name)
        print(self.park_states)
        print(self.park_activities)
        print(self.park_amenities)
        print(self.park_amenities_urls)

        # self.park_information = park_information
        # self.park_url = park_url
        # self.park_phone_number = park_phone_number
        # self.park_tty_number = park_tty_number
        # self.park_email_address = park_email_address

    # def display_park(self):
    #     print(self.park_name, self.park_state, self.park_activities, self.park_amenities, self.park_amenities_urls,
    #           self.park_campground_name)
        #print('Name: {},   State: {},   Information: {}'.format(park.park_name, park.park_state, park.park_information))
        # return self.park_name + ", " + self.park_state + ", " + self.park_activities + ", " + self.park_amenities + ", " + \
        #        self.park_amenities_urls + ", " + self.park_campground_name
