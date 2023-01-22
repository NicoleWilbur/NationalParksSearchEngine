from decrypt_key import key_decryption
from api_pandas import APIPandas
from gui_class import GUIInterface
from tkinter import messagebox


def main():
    try:
        api_key = key_decryption()
        data_handler = APIPandas(api_key)
        data_handler.get_api_data()
        distinct_activities, distinct_amenities, distinct_parks, distinct_states = data_handler.fetch_dropdown_list_data()
    except:
        messagebox.showinfo(
            message='API Key Error. If problem continues, request new API Key from developer.')

    try:
        gui_init = GUIInterface(data_handler, distinct_activities, distinct_amenities, distinct_parks, distinct_states)
        gui_init.load_frame1()
    except:
        messagebox.showinfo(
            message='Tkinter Error. If problem continues, contact developer.')

if __name__ == '__main__':
    main()
