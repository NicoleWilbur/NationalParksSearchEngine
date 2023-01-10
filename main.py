from db_connection import MySQLConnector
from api_data import *
from gui_class import GUIInterface
from decrypt_key import key_decryption
from api_pandas import APIPandas
from results_object import ParkResults


def main():

    user_host = "localhost"
    user_name = "root"
    user_password = "!Password1"


    #
    # my_init_cnxn = MySQLConnector(user_host, user_name, user_password)
    #
    #
    # MySQLConnector.new_database(my_init_cnxn)
    # MySQLConnector.new_tables(my_init_cnxn)
    #
    # function_list = [get_activities_parks(), get_amenities_parks(), get_amenities_visitor_center(), get_campgrounds(),
    #                  get_parkinglots(), get_places()]
    #
    # for function in function_list:
    #     MySQLConnector.populate_tables(my_init_cnxn, function)
    #
    # distinct_activities, distinct_amenities, distinct_parks, distinct_states = MySQLConnector.fetch_dropdown_list_data(my_init_cnxn)
    #
    # GUIInterface(distinct_activities, distinct_amenities, distinct_parks, distinct_states, my_init_cnxn)

    api_key = key_decryption()
    data_handler = APIPandas(api_key)
    data_handler.get_data()
    distinct_activities, distinct_amenities, distinct_parks, distinct_states = data_handler.fetch_dropdown_list_data()
    #ParkResults(data_handler.fetch_results(['Wildlife Watching', 'Arts and Culture'], ['Restroom'], ['Acadia National Park'], ['ME']))
    ParkResults.display_park(ParkResults(data_handler.fetch_results(['Wildlife Watching', 'Arts and Culture'], ['Restroom'], ['Acadia National Park'], ['ME'])))
    # print(distinct_parks)
    # print(distinct_states)

if __name__ == '__main__':
    main()