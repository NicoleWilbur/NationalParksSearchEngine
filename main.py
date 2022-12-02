from db_connection import MySQLConnector
from api_data import *
from gui_class import GUIInterface
from decrypt_key import key_decryption
from api_pandas import APIPandas

# def print_to_file(insert_statement):
#     with open('config.txt', 'a') as f:
#         f.write(insert_statement)
#         # for item in results:
#         #     f.write('')
#         #     f.write('Park Name: ' + item['fullName'])
#         #
#         # for place in item['places']:
#         #     f.write('    Place: ' + place['title'])
#         #     f.write('        For More Information: ' + place['url'])
#     f.close()

# def authorization():
#     discogs_oauth_key = os.getenv("API_KEY")
#
#     oauth = f'OAuth oauth_api_key="{discogs_oauth_key}",oauth_token="{discogs_token}",' \
#         'oauth_signature_method="HMAC-SHA1",' \
#         'oauth_version="1.0"'
#
#     return oauth




# def get_parks_results(my_init_cnxn, distinct_activities):  #eventual parks object
#     parks_list = MySQLConnector.fetch_results(my_init_cnxn, distinct_activities)
#     print(parks_list)


def main():

    user_host = "localhost"
    user_name = "root"
    user_password = "!Password1"
    user_database_name = None


    #
    # my_init_cnxn = MySQLConnector(user_host, user_name, user_password, user_database_name)

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
    print(api_key)
    api_connection = APIPandas()

    api_connection.get_data()

if __name__ == '__main__':
    main()