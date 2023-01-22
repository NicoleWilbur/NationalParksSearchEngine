import math

import pandas as pd


class ParkResults:
    @staticmethod
    def convert_tuple(tup):
        string = ''
        for i in range(len(tup)):

            if isinstance(tup[i], str):
                string += tup[i]
            else:
                string += 'No Data'
        return string

    def __init__(self):
        pass

    @classmethod
    def param_constructor(cls, park_info_df, campground_results_df, parking_lot_results_df):
        cls.results_list = []
        cls.park = ""
        cls.state = ""
        cls.amenities = ""
        cls.campname = ""
        cls.roads = ''
        cls.camptype = ''
        cls.campADA = ''
        cls.wheelchair = ''
        cls.rvinfo = ''
        cls.campdesc = ''
        cls.cellreception = ''
        cls.campstore = ''
        cls.internet = ''
        cls.water = ''
        cls.toilet = ''
        cls.electricity = ''
        cls.staffvolunteer = ''
        cls.lotname = ''
        cls.adainfo = ''
        cls.adaaccess = ''
        cls.oversizedspaces = ''
        cls.adaspaces = ''
        cls.stepfreespaces = ''
        cls.vanspaces = ''
        cls.lotdescription = ''

        for park_row in park_info_df.iterrows():
            park = park_row[1]["park_name"]
            cls.park = list(park)[0]
            state = "  State(s): ", ", ".join(park_row[1]["park_states"])
            cls.state = cls.convert_tuple(state)
            # print("  Activities: ")
            # print(", ".join(park_row[1]["activity_name"]))
            cls.amenities = "  Amenities: \n  "
            cls.amenities += ", ".join(park_row[1]["amenity_name"])

            for park_code in park_row[1]["park_code"]:
                park_code = park_code
            for camp_row in campground_results_df[campground_results_df["park_code"] == park_code].iterrows():
                campname = "  Campground Name: ", camp_row[1]["campground_name"]
                cls.campname = cls.convert_tuple(campname)
                roads = "    Roads: ", camp_row[1]["campground_road"]
                cls.roads = cls.convert_tuple(roads)
                camptype = "    Type of Campground: ", camp_row[1]["campground_classification"]
                cls.camptype = cls.convert_tuple(camptype)
                campADA = "    ADA Information: ", camp_row[1]["campground_general_ADA"]
                cls.campADA = cls.convert_tuple(campADA)
                wheelchair = "    Wheelchair Access: ", camp_row[1]["campground_wheelchair_access"]
                cls.wheelchair = cls.convert_tuple(wheelchair)
                rvinfo = "    RV Information: ", camp_row[1]["campground_rv_info"]
                cls.rvinfo = cls.convert_tuple(rvinfo)
                campdesc = "    Campground Description: ", camp_row[1]["campground_description"]
                cls.campdesc = cls.convert_tuple(campdesc)
                cellreception = "    Cell Reception: ", camp_row[1]["campground_cell_reception"]
                cls.cellreception = cls.convert_tuple(cellreception)
                campstore = "    Camp Store: ", camp_row[1]["campground_camp_store"]
                cls.campstore = cls.convert_tuple(campstore)
                internet = "    Internet Availability: ", camp_row[1]["campground_internet"]
                cls.internet = cls.convert_tuple(internet)
                water = "    Potable Water Availability: ", camp_row[1]["campground_potable_water"]
                cls.water = cls.convert_tuple(water)
                toilet = "    Toilet Information: ", camp_row[1]["campground_toilets"]
                cls.toilet = cls.convert_tuple(toilet)
                electricity = "    Number of Electric Sites: ", camp_row[1]["campground_campsites_electric"]
                cls.electricity = cls.convert_tuple(electricity)
                staffvolunteer = "    Staff or Volunteer Present: ", camp_row[1]["campground_staff_volunteer"]
                cls.staffvolunteer = cls.convert_tuple(staffvolunteer)
            for lot_row in parking_lot_results_df[parking_lot_results_df["park_code"] == park_code].iterrows():
                lotname = "  Parking Lot: ", lot_row[1]["parking_lots_name"]
                cls.lotname = cls.convert_tuple(lotname)
                adainfo = "    ADA Information: ", lot_row[1]["parking_lots_ADA_facility_description"]
                cls.adainfo = cls.convert_tuple(adainfo)
                adaaccess = "    ADA Accessible?: ", lot_row[1]["parking_lots_is_lot_accessible"]
                cls.adaaccess = cls. convert_tuple(adaaccess)
                oversizedspaces = "    Number of Over-Sized Spaces:  ", lot_row[1]["parking_lots_number_oversized_spaces"]
                cls.oversizedspaces = cls.convert_tuple(oversizedspaces)
                adaspaces = "    Number of ADA Spaces: ", lot_row[1]["parking_lots_number_ADA_spaces"]
                cls.adaaccess = cls.convert_tuple(adaspaces)
                stepfreespaces = "    Number of ADA Step-Free Spaces: ", lot_row[1]["parking_lots_number_ADA_Step_Free_Spaces"]
                cls.stepfreespaces = cls.convert_tuple(stepfreespaces)
                vanspaces = "    Number of ADA Van Spaces: ", lot_row[1]["parking_lots_number_ADA_van_spaces"]
                cls.vanspaces = cls.convert_tuple(vanspaces)
                lotdescription = "    Parking Lot Description: ", lot_row[1]["parking_lots_description"]
                cls.lotdescription = cls.convert_tuple(lotdescription)

            cls.results_list += [cls.park, cls.state, cls.amenities, cls.campname, cls.roads, cls.camptype, cls.campADA,
            cls.wheelchair, cls.rvinfo, cls.campdesc, cls.cellreception, cls.campstore, cls.internet, cls.water, cls.toilet,
            cls.electricity, cls.staffvolunteer, cls.lotname, cls.adainfo, cls.adaaccess, cls.oversizedspaces, cls.adaspaces,
            cls.stepfreespaces, cls.vanspaces, cls.lotdescription]