from db_connection import MySQLConnector
from api_data import *
from gui_class import GUIInterface
from decrypt_key import *


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

    api_key = decrypt_key()
    print(api_key)

    # initialize url, query string, and headers
    url = "https://covid-19-data.p.rapidapi.com/totals"
    qrystr = {'format': "json"}
    hdrs = {
        'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
        'x-rapidapi-key': api_key
    }

    my_init_cnxn = MySQLConnector(user_host, user_name, user_password, user_database_name)

    MySQLConnector.new_database(my_init_cnxn)
    MySQLConnector.new_tables(my_init_cnxn)

    function_list = [get_activities_parks(), get_amenities_parks(), get_amenities_visitor_center(), get_campgrounds(),
                     get_parkinglots(), get_places()]

    for function in function_list:
        MySQLConnector.populate_tables(my_init_cnxn, function)


    ###########dont use the below
    # insert_statement = get_thingstodo()
    # # print(insert_statement)
    # MySQLConnector.populate_tables(my_init_cnxn, insert_statement)
    #
    # insert_statement = get_topics_parks()
    # # print(insert_statement)
    # MySQLConnector.populate_tables(my_init_cnxn, insert_statement)

    distinct_activities, distinct_amenities, distinct_parks, distinct_states = MySQLConnector.fetch_dropdown_list_data(my_init_cnxn)

    # print(distinct_activities)
    # print(distinct_amenities)
    # print(distinct_parks)
    # print(distinct_states)
    GUIInterface(distinct_activities, distinct_amenities, distinct_parks, distinct_states, my_init_cnxn)
    # try:
    #     MySQLConnector.delete_database(my_init_cnxn)
    #     print("Database deleted.")
    # except ConnectionError:
    #     print("Database not deleted.")
    #     MySQLConnector.delete_database(my_init_cnxn)


    # for i in self.parks_list:  #eventual parks object
    #     results = tk.Label(
    #         self.frame2,
    #         text=i,
    #         bg="#28393a",
    #         fg=self.fg_color,
    #         font=("TkTextFont", 12)
    #     )
    #     results.pack(fill="both")

    #gui = Interface(distinct_activities)
    #InterfaceClass.display(gui_interface)
    # load the first frame
    #GUI.load_frame1(distinct_activities)

if __name__ == '__main__':
    main()