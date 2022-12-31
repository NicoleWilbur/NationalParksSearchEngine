###the correct package to install is mysql-connector-python
import mysql.connector
from mysql.connector import Error
from results_object import ParkResults


# Add connection
class MySQLConnector:

    def __init__(self, user_host, user_name, user_password):
        try:
            self.__conn = mysql.connector.connect(
                host=user_host,
                user=user_name,
                password=user_password)
            print("Connected to server.")
        except ConnectionRefusedError:
            print("Connection refused; please check connection settings and try again.")

    def new_database(self):
        try:
            __cursor = self.__conn.cursor()
            __cursor.execute("CREATE DATABASE IF NOT EXISTS NPS_API_Data;")
            print("2")
            print("Database created.")
        except Error:
            print("1: Connection interrupted; please try again.")
        finally:
            __cursor.close()

    def new_tables(self):
        try:
            __cursor = self.__conn.cursor()
            __cursor.execute("CREATE TABLE IF NOT EXISTS NPS_API_Data.activities_parks ("
                             "park_code varchar(50),"
                             "park_states varchar(50),"
                             "park_name varchar(250),"
                             "activity_name varchar(250))")
            print("activities_parks table created.")
            __cursor.execute("CREATE TABLE IF NOT EXISTS NPS_API_Data.amenities_parks ("
                             "park_code varchar(50),"
                             "amenity varchar(250),"
                             "url varchar(250)) ")
            print("amenities_parks table created.")
            __cursor.execute("CREATE TABLE IF NOT EXISTS NPS_API_Data.amenities_visitor_center ("
                             "park_code varchar(50),"
                             "amenity varchar(250),"
                             "visitor_center_name varchar(250),"
                             "url varchar(250)) ")
            print("amenities_visitor_center tables created.")
            __cursor.execute("CREATE TABLE IF NOT EXISTS NPS_API_Data.campgrounds ("
                             "park_code varchar (50),"
                             "paved_roads varchar(250),"
                             "general_ADA varchar(1000),"
                             "campground_classification varchar(250),"
                             "wheelchair_access_campground varchar(500),"
                             "rv_allowed int,"
                             "rv_info varchar(500),"
                             "rv_max_length int,"
                             "trailers_allowed int,"
                             "trailer_max_length int,"
                             "description varchar(1000),"
                             "campground_id varchar(250),"
                             "campsite_name varchar(250),"
                             "url varchar(250),"
                             "cell_reception varchar(250),"
                             "camp_store varchar(250),"
                             "dump_station varchar(250),"
                             "internet varchar(250),"
                             "potable_water varchar(250),"
                             "showers varchar(250),"
                             "toilets varchar(250),"
                             "campsites_electric int,"
                             "campsites_group int,"
                             "campsites_horse int,"
                             "campsites_other int,"
                             "campsites_rv_only int,"
                             "campsites_tent_only int,"
                             "campsites_boat_access int,"
                             "total_sites int,"
                             "staff_volunteer varchar (250)) ")
            print("campgrounds table created.")
            __cursor.execute("CREATE TABLE IF NOT EXISTS NPS_API_Data.parking_lots ("
                             "lot_id varchar(50),"
                             "lot_name varchar(250),"
                             "park_code varchar(50),"
                             "ada_description varchar(500),"
                             "ada_accessible varchar(25),"
                             "over_sized_spaces int,"
                             "general_ada_spaces int,"
                             "step_free_ada_spaces int,"
                             "ada_van_spaces int,"
                             "lot_description varchar(1000)) ")
            print("parking_lots table created.")
            __cursor.execute("CREATE TABLE IF NOT EXISTS NPS_API_Data.places ("
                             "place_id varchar(50),"
                             "place_name varchar(250),"
                             "url varchar(250),"
                             "park_code varchar(50)) ")
            print("places table created.")

        except ConnectionError:
            print("2: Connection interrupted; please try again.")
        finally:
            __cursor.close()

    def populate_tables(self, insert_statement):
        try:
            __cursor = self.__conn.cursor()
            __cursor.execute(insert_statement)
            self.__conn.commit()
        except ConnectionError:
            print("Database: Connection interrupted; please try again.")
        finally:
            __cursor.close()
            #self.__conn.close()

    def fetch_dropdown_list_data(self):
        distinct_activities_parks = []
        distinct_amenity = []
        distinct_park = []
        distinct_state = []

        try:
            __cursor = self.__conn.cursor()

            __cursor.execute("SELECT DISTINCT activity_name FROM NPS_API_DATA.activities_parks ORDER BY activity_name;")
            for activity_name in list(__cursor):
                distinct_activities_parks += activity_name

            __cursor.execute("SELECT DISTINCT amenity FROM NPS_API_DATA.amenities_parks ORDER BY amenity;")
            for amenity_name in list(__cursor):
                distinct_amenity += amenity_name

            __cursor.execute("SELECT DISTINCT park_name FROM NPS_API_DATA.activities_parks ORDER BY park_name;")
            for park_name in list(__cursor):
                distinct_park += park_name

            __cursor.execute("SELECT DISTINCT park_states FROM NPS_API_DATA.activities_parks WHERE LENGTH(park_states) = 2 "
                             "ORDER BY park_states;")
            for state in list(__cursor):
                distinct_state += state

        except ConnectionError:
            print("4: Connection interrupted; please try again.")
        finally:
            __cursor.close()

        return distinct_activities_parks, distinct_amenity, distinct_park, distinct_state

    def fetch_results(self, activities_selection, amenities_selection, states_selection, parks_selection):
        park_list = []
        where_logic = ""

        try:
            __cursor = self.__conn.cursor()

            select_statement = "SELECT DISTINCT park_name, activity_name, amenity FROM NPS_API_Data.activities_parks a " \
                      "LEFT JOIN NPS_API_DATA.amenities_parks b ON a.park_code = b.park_code WHERE"

            if activities_selection:
                where_logic = " activity_name IN ("     #df[df['col_1'].isin([1,2,3])]
                if len(activities_selection) > 1:
                    for activity in activities_selection[:-1]:
                        where_logic += "'" + activity + "'" + ','
                where_logic += "'" + activities_selection[-1] + "') "

                if amenities_selection or states_selection or parks_selection:
                    where_logic += "and"

            if amenities_selection:
                where_logic += " amenity in ("
                if len(amenities_selection) > 1:
                    for amenity in amenities_selection[:-1]:
                        where_logic += "'" + amenity + "'" + ','
                where_logic += "'" + amenities_selection[-1] + "') "
                print(where_logic)

                if states_selection or parks_selection:
                    where_logic += "and"
                    print(where_logic)

            if states_selection:
                where_logic += " park_states in ("
                if len(states_selection) > 1:
                    for state in states_selection[:-1]:
                        where_logic += "'" + state + "'" + ','
                where_logic += "'" + states_selection[-1] + "') "

                if parks_selection:
                    where_logic += "and"

            if parks_selection:
                where_logic += " park_name in ("
                if len(parks_selection) > 1:
                    for park in parks_selection[:-1]:
                        where_logic += "'" + park + "'" + ','
                where_logic += "'" + parks_selection[-1] + "') "

            select_statement += where_logic + "ORDER BY park_name"
            print(select_statement)
            __cursor.execute(select_statement)

            for park_name in list(__cursor):
                #park_list += park_name
                park_state = "foo"
                park_information = "boo"
                park_list.append(ParkResults(park_name[0], park_state, park_information))
            print("A")

            # for park in park_list:
            #     print('Name: {},   State: {},   Information: {}'.format(park.park_name, park.park_state, park.park_information))

            # ParkResults.display_park(park_list)
            # ParkResults.save_to_file(park_list)
        except ConnectionError:
            print("4: Connection interrupted; please try again.")
        finally:
            __cursor.close()

        return park_list

    def delete_database(self):
        try:
            __cursor = self.__conn.cursor()
            __cursor.execute("DROP DATABASE IF EXISTS NPS_API_Data;")
        except ConnectionError:
            print("Connection interrupted; please try again.")
        finally:
            __cursor.close()
