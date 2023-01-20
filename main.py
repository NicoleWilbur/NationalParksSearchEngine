from decrypt_key import key_decryption
from api_pandas import APIPandas
from gui_class import GUIInterface



def main():

    api_key = key_decryption()
    data_handler = APIPandas(api_key)
    data_handler.get_api_data()
    distinct_activities, distinct_amenities, distinct_parks, distinct_states = data_handler.fetch_dropdown_list_data()
    gui_init = GUIInterface(data_handler, distinct_activities, distinct_amenities, distinct_parks, distinct_states)
    gui_init.load_frame1()


if __name__ == '__main__':
    main()