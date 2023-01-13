from decrypt_key import key_decryption
from api_pandas import APIPandas
from park_results import ParkResults


def main():

    api_key = key_decryption()
    data_handler = APIPandas(api_key)
    data_handler.get_data()
    distinct_activities, distinct_amenities, distinct_parks, distinct_states = data_handler.fetch_dropdown_list_data()
    ParkResults(data_handler.fetch_results(['Wildlife Watching', 'Arts and Culture'], ['Restroom'], ['Acadia National Park'], ['ME']))
    # ParkResults.display_park(ParkResults(data_handler.fetch_results(['Wildlife Watching', 'Arts and Culture'], ['Restroom'], ['Acadia National Park'], ['ME'])))
    # print(distinct_parks)
    # print(distinct_states)

if __name__ == '__main__':
    main()