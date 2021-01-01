import tkinter as tk

WIDTH = 75


class AddressEntry(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.address_lbl = tk.Label(self, text='Address')
        self.address_lbl.pack(side=tk.LEFT, anchor='w')

        self.address_entry = tk.Entry(self, width=WIDTH)
        self.address_entry.pack(side=tk.LEFT)

    def set_data(self, data):
        self.address_entry.insert(0, data)

    def get_data(self):
        # Return the text entered in entry field
        return self.address_entry.get()

    def clear_data(self):
        # Delete the text entered in entry field
        self.address_entry.delete(0, 'end')
