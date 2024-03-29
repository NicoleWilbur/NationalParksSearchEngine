import datetime
import os
import tkinter as tk
from tkinter import LEFT, BOTH, RIGHT, END, X, TOP, messagebox

from api_pandas import APIPandas
from park_results import ParkResults

class GUIInterface:

    def __init__(self, data_handler, distinct_activities, distinct_amenities, distinct_parks, distinct_states):
        self.data_handler = data_handler
        self.activities_list = distinct_activities
        self.amenities_list = distinct_amenities
        self.name_list = distinct_parks
        self.states_list = distinct_states
        self.parks_list = distinct_parks
        self.activities_selection = []
        self.parks_selection = []
        self.states_selection = []
        self.amenities_selection = []
        self.results_for_gui = ''

        self.root = tk.Tk()
        self.root.title('National Parks Service Search Engine')
        self.root.geometry('+50+50')
        # self.root.eval('tk::PlaceWindow %s center' % self.root.winfo_pathname(self.root.winfo_id()))

        # color scheme
        self.bg_color = '#bf5720'
        self.fg_color = 'White'

        # create a frame widgets
        self.frame1 = tk.Frame(self.root, width=1000, height=600, bg=self.bg_color)
        self.frame2 = tk.Frame(self.root, bg=self.bg_color)

        # place frame widgets in window
        for frames in (self.frame1, self.frame2):
            frames.grid(row=0, column=0)

        # initiallize app with basic settings
        self.load_frame1()

        # run app
        self.root.mainloop()

    def clear_widgets(self, frame):
        # select all frame widgets and delete them
        for widget in frame.winfo_children():
            widget.destroy()

    def get_activities_selection(self, activities_listbox):
        for i in activities_listbox.curselection():
            self.activities_selection.append(activities_listbox.get(i))
        return self.activities_selection

    def get_amenities_selection(self, amenities_listbox):
        for i in amenities_listbox.curselection():
            self.amenities_selection.append(amenities_listbox.get(i))
        return self.amenities_selection

    def get_states_selection(self, states_listbox):
        for i in states_listbox.curselection():
            self.states_selection.append(states_listbox.get(i))
        return self.states_selection

    def get_parks_selection(self, parks_listbox):
        for i in parks_listbox.curselection():
            self.parks_selection.append(parks_listbox.get(i))
        return self.parks_selection

    def selection_check(self, activities_selection, amenities_selection, states_selection, parks_selection):
        if not activities_selection and not amenities_selection and not states_selection and not parks_selection:
            messagebox.showinfo(message='Please choose at least one item.')
        else:
            results_check = self.get_results()
            print(results_check)
            if results_check:
                self.load_frame2()
    def get_results(self):

        park_info_df, campground_results_df, parking_lot_results_df = self.data_handler.fetch_results(
            self.activities_selection, self.amenities_selection, self.parks_selection, self.states_selection)

        if park_info_df.empty and campground_results_df.empty and parking_lot_results_df.empty:
            messagebox.showinfo(message='No results found. Try a different search.')
            self.activities_selection.clear(), self.amenities_selection.clear(),
            self.states_selection.clear(), self.parks_selection.clear()

        else:
            self.results_for_gui = ParkResults.param_constructor(park_info_df, campground_results_df, parking_lot_results_df)

        return self.results_for_gui

    def save_to_file(self, results):
        current_time = datetime.datetime.now()
        try:
            if os.path.exists('National Parks Search Results.txt'):
                messagebox.showinfo(message='National Parks Search Results.txt Already Exists. Results will be saved to '
                                            'end of that file unless file is deleted or contents erased.')
            with open('National Parks Search Results.txt', 'a') as f:
                print('foo')
                f.write('Search Results as of: ' + str(current_time) + '\n\n' + results)
            messagebox.showinfo(message='National Parks Search Results.txt Saved')
            f.close()
        except:
            messagebox.showinfo(message='boo')

    def close_button(self, frame):
        close = tk.Button(
            frame,
            text='Close',
            font=('TkTextFont', 12),
            fg='black',
            cursor='hand2',
            activeforeground=self.bg_color,
            command=lambda: [self.root.quit()]
        )
        close.pack(side=TOP, pady=10)

    def load_frame1(self):
        self.clear_widgets(self.frame2)
        self.frame1.tkraise()
        # prevents child from modifying parent
        self.frame1.pack_propagate(False)

        # in frame label widget
        tk.Label(
            self.frame1,
            text='Search Options',
            bg=self.bg_color,
            fg=self.fg_color,
            font=('TkMenuFont', 14)
        ).pack()

        # subframes for layout and packing
        frame1a = tk.Frame(self.frame1)  # activities/amenities lables
        frame1a.pack()
        frame1b = tk.Frame(self.frame1)  # activities/amenities boxes
        frame1b.pack()
        frame1c = tk.Frame(self.frame1)  # states/parks lables
        frame1c.pack()
        frame1d = tk.Frame(self.frame1)  # states/parkes boxes
        frame1d.pack()

        # list conversions/prep
        activities_var = tk.StringVar(value=self.activities_list)
        amenities_var = tk.StringVar(value=self.amenities_list)
        states_var = tk.StringVar(value=self.states_list)
        parks_var = tk.StringVar(value=self.parks_list)

        # search box labels
        activities_label = tk.Label(frame1a, text='Select activities:  ', font=('TkHeaderFont', 10),
                                    bg=self.bg_color, fg=self.fg_color, padx=30, pady=10)
        activities_label.pack(expand=True, anchor='center', side=LEFT)

        amenities_label = tk.Label(frame1a, text='Select amenities:  ', font=('TkHeaderFont', 10),
                                   bg=self.bg_color, fg=self.fg_color, padx=30, pady=10)
        amenities_label.pack(expand=True, anchor='center', side=RIGHT)

        states_label = tk.Label(frame1c, text='Select states/territories:  ', font=('TkHeaderFont', 10),
                                bg=self.bg_color, fg=self.fg_color, padx=30, pady=10)
        states_label.pack(expand=True, fill=BOTH, side=LEFT)

        parks_label = tk.Label(frame1c, text='Select parks:  ', font=('TkHeaderFont', 10),
                               bg=self.bg_color, fg=self.fg_color, padx=30, pady=10)
        parks_label.pack(expand=True, fill=BOTH, side=LEFT)

        # list boxes and scroll bars
        activities_listbox = tk.Listbox(
            frame1b,
            listvariable=activities_var,
            selectmode='multiple',
            exportselection=False,
            width=30)
        activities_listbox.pack(expand=True, fill=X, side=LEFT)

        # creates a scrollbar and attaches it to frame1b window
        activities_scrollbar = tk.Scrollbar(frame1b)
        activities_scrollbar.pack(expand=True, fill=BOTH, side=LEFT)
        # Attaching Listbox to Scrollbar Since we need to have a vertical scroll we use yscrollcommand
        activities_listbox.config(yscrollcommand=activities_scrollbar.set)
        # setting scrollbar command parameter to listbox.yview method its yview because we need to have a vertical view
        activities_scrollbar.config(command=activities_listbox.yview)

        spacer = tk.Label(frame1b, bg=self.bg_color, fg=self.fg_color, padx=30, pady=10)
        spacer.pack(expand=True, fill=BOTH, side=LEFT)

        amenities_listbox = tk.Listbox(
            frame1b,
            listvariable=amenities_var,
            selectmode='multiple',
            exportselection=False,
            width=30)
        amenities_listbox.pack(expand=True, fill=X, side=LEFT)

        # creates a scrollbar and attaches it
        amenities_scrollbar = tk.Scrollbar(frame1b)
        amenities_scrollbar.pack(expand=True, fill=BOTH, side=LEFT)
        # Attaching Listbox to Scrollbar Since we need to have a vertical scroll we use yscrollcommand
        amenities_listbox.config(yscrollcommand=amenities_scrollbar.set)
        # setting scrollbar command parameter to listbox.yview method its yview because we need to have a vertical view
        amenities_scrollbar.config(command=amenities_listbox.yview)

        states_listbox = tk.Listbox(
            frame1d,
            listvariable=states_var,
            selectmode='multiple',
            exportselection=False,
            width=30)
        states_listbox.pack(expand=True, fill=BOTH, side=LEFT)
        # creates a scrollbar and attaches it
        states_scrollbar = tk.Scrollbar(frame1d)
        states_scrollbar.pack(expand=True, fill=BOTH, side=LEFT)
        # Attaching Listbox to Scrollbar Since we need to have a vertical scroll we use yscrollcommand
        states_listbox.config(yscrollcommand=states_scrollbar.set)
        # setting scrollbar command parameter to listbox.yview method its yview because we need to have a vertical view
        states_scrollbar.config(command=states_listbox.yview)

        spacer = tk.Label(frame1d, bg=self.bg_color, fg=self.fg_color, padx=30, pady=10)
        spacer.pack(expand=True, fill=BOTH, side=LEFT)

        parks_listbox = tk.Listbox(
            frame1d,
            listvariable=parks_var,
            selectmode='multiple',
            exportselection=False,
            width=30)
        parks_listbox.pack(expand=True, fill=BOTH, side=LEFT)

        # creates a scrollbar and attaches it
        parks_scrollbar = tk.Scrollbar(frame1d)
        parks_scrollbar.pack(expand=True, fill=BOTH, side=LEFT)
        # Attaching Listbox to Scrollbar Since we need to have a vertical scroll we use yscrollcommand
        parks_listbox.config(yscrollcommand=parks_scrollbar.set)
        # setting scrollbar command parameter to listbox.yview method its yview because we need to have a vertical view
        parks_scrollbar.config(command=parks_listbox.yview)

        # macOS bug with Tkinter: button backgrounds do not work unless use tkmacos; leaving for Windows compatibility
        search = tk.Button(
            self.frame1,
            text='Fetch!',
            font=('TkTextFont', 12),
            fg='black',
            cursor='hand2',
            activeforeground=self.bg_color,
            command=lambda: [self.selection_check(self.get_activities_selection(activities_listbox),
                                                  self.get_amenities_selection(amenities_listbox),
                                                  self.get_states_selection(states_listbox),
                                                  self.get_parks_selection(parks_listbox))]
        )
        search.pack(pady=20)
        self.close_button(self.frame1)

    def load_frame2(self):
        self.clear_widgets(self.frame1)
        self.frame2.tkraise()

        back = tk.Button(
            self.frame2,
            text='Back',
            font=('TkTextFont', 12),
            fg='black',
            cursor='hand2',
            activeforeground=self.bg_color,
            command=lambda: [self.load_frame1(), self.activities_selection.clear(), self.amenities_selection.clear(),
                             self.states_selection.clear(), self.parks_selection.clear()]
        )
        back.pack(side=TOP, pady=10)

        # create label widget for instructions
        tk.Label(
            self.frame2,
            text='Results',
            bg=self.bg_color,
            fg=self.fg_color,
            font=('TkHeadingFont', 20)
        ).pack(side=TOP, pady=10)

        search_parameters = self.activities_selection + self.amenities_selection + self.states_selection + self.parks_selection
        string_parameters = ''
        for parameter in search_parameters:
            string_parameters += parameter + ', '
        string_parameters = string_parameters[:-2]

        tk.Label(self.frame2,
                 text='Parks Meeting Your Search of:\n' + string_parameters,
                 bg=self.bg_color,
                 fg=self.fg_color,
                 font=('TkTextFont', 12)
                 ).pack()

        frame2a = tk.Frame(self.frame2)
        frame2a.pack(fill=X)

        frame2a.grid_columnconfigure(0, weight=50)
        frame2a.grid_columnconfigure(1, weight=1)

        # creates a scrollbar and attaches it to frame2a window
        scrollbar = tk.Scrollbar(frame2a)
        scrollbar.pack(side=RIGHT, fill=BOTH)

        resultsbox = tk.Text(frame2a, yscrollcommand=scrollbar.set)

        # Attaching Listbox to Scrollbar Since we need to have a vertical scroll we use yscrollcommand
        resultsbox.config(yscrollcommand=scrollbar.set)

        # setting scrollbar command parameter to listbox.yview method its yview because we need to have a vertical view
        scrollbar.config(command=resultsbox.yview)

        resultsbox.insert(END, self.results_for_gui)
        resultsbox.pack()

        # creates close and print button widgets
        save_results = tk.Button(
            self.frame2,
            text='Save',
            font=('TkTextFont', 12),
            fg='black',
            cursor='hand2',
            activeforeground=self.bg_color,
            command=lambda: self.save_to_file(self.results_for_gui)
        )
        save_results.pack(side=TOP, pady=10)

        self.close_button(self.frame2)
