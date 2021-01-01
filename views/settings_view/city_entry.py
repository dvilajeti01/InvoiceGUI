import tkinter as tk

WIDTH = 50


class CityEntry(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.city_lbl = tk.Label(self, text='City')
        self.city_lbl.pack(side=tk.LEFT, anchor='w')

        self.city_entry = tk.Entry(self, width=WIDTH)
        self.city_entry.pack(side=tk.LEFT)

    def set_data(self, data):
        self.city_entry.insert(0, data)

    def get_data(self):
        # Return the text entered in entry field
        return self.city_entry.get()

    def clear_data(self):
        # Delete the text entered in entry field
        self.city_entry.delete(0, 'end')
