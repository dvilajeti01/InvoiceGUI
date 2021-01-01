import tkinter as tk

WIDTH = 50


class NameEntry(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.name_lbl = tk.Label(self, text='Name')
        self.name_lbl.pack(side=tk.LEFT, anchor='w')

        self.name_entry = tk.Entry(self, width=WIDTH)
        self.name_entry.pack(side=tk.LEFT)

    def set_data(self, data):
        self.name_entry.insert(0, data)

    def get_data(self):
        # Return the text entered in entry field
        return self.name_entry.get()

    def clear_data(self):
        # Delete the text entered in entry field
        self.name_entry.delete(0, 'end')
