import tkinter as tk
from tkinter import LEFT, BOTH, RIGHT, END, X, TOP, messagebox

from api_pandas import APIPandas


class GUIInterface:

    def __init__(self, distinct_activities, distinct_amenities, distinct_parks, distinct_states, my_init_cnxn):
        self.database_connection = my_init_cnxn
        self.activities_list = distinct_activities
        self.amenities_list = distinct_amenities
        self.name_list = distinct_parks
        self.states_list = distinct_states
        self.parks_list = distinct_parks
        self.activities_selection = []
        self.parks_selection = []
        self.states_selection = []
        self.amenities_selection = []

        self.root = tk.Tk()
        self.root.title("National Parks Service Search Engine")
        self.root.geometry("+50+50")
        # self.root.eval('tk::PlaceWindow %s center' % self.root.winfo_pathname(self.root.winfo_id()))

        # color scheme
        self.bg_color = "#bf5720"
        self.fg_color = "White"

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
            messagebox.showerror("No Selections Chosen", "Please choose at least one item.")
        else:
            self.load_frame2()

    def save_to_file(self, results_list):
        with open('config.txt', 'a') as f:
            for result in results_list:
                f.write('Name : {} Information : {}'.format(result.park_name, result.park_information) + "\n\n")
        f.close()

    def close_button(self, frame):
        close = tk.Button(
            frame,
            text="Close",
            font=("TkTextFont", 12),
            fg="black",
            cursor="hand2",
            activeforeground=self.bg_color,
            command=lambda: [self.root.destroy()]
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
            text="Search Options",
            bg=self.bg_color,
            fg=self.fg_color,
            font=("TkMenuFont", 14)
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
        activities_label = tk.Label(frame1a, text="Select activities:  ", font=("TkHeaderFont", 10),
                                    bg=self.bg_color, fg=self.fg_color, padx=30, pady=10)
        activities_label.pack(expand=True, fill=BOTH, side=LEFT)

        amenities_label = tk.Label(frame1a, text="Select amenities:  ", font=("TkHeaderFont", 10),
                                   bg=self.bg_color, fg=self.fg_color, padx=30, pady=10)
        amenities_label.pack(expand=True, fill=BOTH, side=LEFT)

        states_label = tk.Label(frame1c, text="Select states/territories:  ", font=("TkHeaderFont", 10),
                                bg=self.bg_color, fg=self.fg_color, padx=30, pady=10)
        states_label.pack(expand=True, fill=BOTH, side=LEFT)

        parks_label = tk.Label(frame1c, text="Select parks:  ", font=("TkHeaderFont", 10),
                               bg=self.bg_color, fg=self.fg_color, padx=30, pady=10)
        parks_label.pack(expand=True, fill=BOTH, side=LEFT)

        # list boxes and scroll bars
        activities_listbox = tk.Listbox(
            frame1b,
            listvariable=activities_var,
            selectmode="multiple",
            exportselection=False,
            width=30)
        activities_listbox.pack(expand=True, fill=X, side=LEFT)

        # creates a scrollbar and attaches it to frame1a window
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
            selectmode="multiple",
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
            selectmode="multiple",
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

        parks_listbox = tk.Listbox(
            frame1d,
            listvariable=parks_var,
            selectmode="multiple",
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
            text="Fetch!",
            font=("TkTextFont", 12),
            fg="black",
            cursor="hand2",
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

        results_list = APIPandas.fetch_results(self.database_connection, self.activities_selection,
                                                       self.amenities_selection, self.states_selection,
                                                       self.parks_selection)

        back = tk.Button(
            self.frame2,
            text="Back",
            font=("TkTextFont", 12),
            fg="black",
            cursor="hand2",
            activeforeground=self.bg_color,
            command=lambda: [self.load_frame1(), self.activities_selection.clear(), self.amenities_selection.clear(),
                             self.states_selection.clear(), self.parks_selection.clear()]
        )
        back.pack(side=TOP, pady=10)

        # create label widget for instructions
        tk.Label(
            self.frame2,
            text="Results",
            bg=self.bg_color,
            fg=self.fg_color,
            font=("TkHeadingFont", 20)
        ).pack(side=TOP, pady=10)

        tk.Label(self.frame2,
                 text="Parks Meeting Your Search of:\n" + str(self.activities_selection) + "\n" + str(
                     self.amenities_selection),
                 bg=self.bg_color,
                 fg=self.fg_color,
                 font=("TkTextFont", 12)
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

        i = 1
        for result in results_list:
            # print('Name : {}, Information : {}'.format(park.park_name, park.park_information))
            # parks_var = tk.StringVar(value='Name : {} Information : {}'.format(park.park_name, park.park_information))
            # # parks_var = tk.StringVar(value=park.display_park())

            resultsbox.insert(END, "Park #" + str(i) + "\n" + 'Name : {} Information : {}'.format(result.park_name,
                                                                                                  result.park_information) +
                              "\n\n")
            resultsbox.pack()
            i += 1

        # creates close and print button widgets
        save_results = tk.Button(
            self.frame2,
            text="Save",
            font=("TkTextFont", 12),
            fg="black",
            cursor="hand2",
            activeforeground=self.bg_color,
            command=lambda: self.save_to_file(results_list)
        )
        save_results.pack(side=TOP, pady=10)

        self.close_button(self.frame2)
