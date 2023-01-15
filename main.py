from decrypt_key import key_decryption
from api_pandas import APIPandas
from gui_class import GUIInterface
from park_results import ParkResults


def main():

    api_key = key_decryption()
    data_handler = APIPandas(api_key)
    data_handler.get_api_data()
    distinct_activities, distinct_amenities, distinct_parks, distinct_states = data_handler.fetch_dropdown_list_data()
    # print(distinct_activities)
    # print(distinct_amenities)
    # print(distinct_parks)
    # print(distinct_states)
    gui_init = GUIInterface(data_handler, distinct_activities, distinct_amenities, distinct_parks, distinct_states)
    gui_init.load_frame1()
    # park_info_dictionary, campground_info_dictionary, places_info_dictionary, parking_lot_info_dictionary = \
    #     data_handler.fetch_results(['Wildlife Watching', 'Arts and Culture'], ['Restroom'], ['Acadia National Park'], ['ME'])
    # ParkResults(park_info_dictionary, campground_info_dictionary, places_info_dictionary, parking_lot_info_dictionary)
    # # print(distinct_parks)
    # print(distinct_states)

if __name__ == '__main__':
    main()