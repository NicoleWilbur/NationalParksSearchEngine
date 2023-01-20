import pandas as pd


class ParkResults:

    def __init__(self):
        self.results_list = ''

    @classmethod
    def param_constructor(cls, park_info_df, campground_results_df, parking_lot_results_df):
        for park_row in park_info_df.iterrows():
            # i = park_row[0]
            park = park_row[1]["park_name"]
            print(list(park)[0])
            print("  State(s): ", ", ".join(park_row[1]["park_states"]))
            # print(", ".join(park_row[1]["park_states"]))
            print("  Activities: ")
            print(", ".join(park_row[1]["activity_name"]))
            print("  Amenities: ")
            print(", ".join(park_row[1]["amenity_name"]))
            for park_code in park_row[1]["park_code"]:
                park_code = park_code
            for camp_row in campground_results_df[campground_results_df["park_code"] == park_code].iterrows():
                print("  ", camp_row[1]["campground_name"])
                print("    Roads: ", camp_row[1]["campground_road"])
                print("    Type of Campground: ", camp_row[1]["campground_classification"])
                print("    ADA Information: ", camp_row[1]["campground_general_ADA"])
                print("    Wheelchair Access: ", camp_row[1]["campground_wheelchair_access"])
                print("    RV Information: ", camp_row[1]["campground_rv_info"])
                print("    Campground Description: ", camp_row[1]["campground_description"])
                print("    Cell Reception: ", camp_row[1]["campground_cell_reception"])
                print("    Camp Store: ", camp_row[1]["campground_camp_store"])
                print("    Internet Availability: ", camp_row[1]["campground_internet"])
                print("    Potable Water Availability: ", camp_row[1]["campground_potable_water"])
                print("    Toilet Information: ", camp_row[1]["campground_toilets"])
                print("    Number of Electric Sites: ", camp_row[1]["campground_campsites_electric"])
                print("    Staff or Volunteer Present: ", camp_row[1]["campground_staff_volunteer"])
            for lot_row in parking_lot_results_df[parking_lot_results_df["park_code"] == park_code].iterrows():
                print("  Parking Lot: ", lot_row[1]["parking_lots_name"])
                print("    ADA Information: ", lot_row[1]["parking_lots_ADA_facility_description"])
                print("    ADA Accessible?: ", lot_row[1]["parking_lots_is_lot_accessible"])
                print("    Number of Over-Sized Spaces:  ", lot_row[1]["parking_lots_number_oversized_spaces"])
                print("    Number of ADA Spaces: ", lot_row[1]["parking_lots_number_ADA_spaces"])
                print("    Number of ADA Step-Free Spaces: ", lot_row[1]["parking_lots_number_ADA_Step_Free_Spaces"])
                print("    Number of ADA Van Spaces: ", lot_row[1]["parking_lots_number_ADA_van_spaces"])
                print("    Parking Lot Description: ", lot_row[1]["parking_lots_description"])
