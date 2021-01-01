import tkinter as tk


class ZipCodeEntry(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.zipcode_lbl = tk.Label(self, text='Zipcode')
        self.zipcode_lbl.pack(side=tk.LEFT, anchor='w')

        self.zipcode_entry = tk.Entry(self)
        self.zipcode_entry.pack(side=tk.LEFT)

    def set_data(self, data):
        self.zipcode_entry.insert(0, data)

    def get_data(self):
        # Return the text entered in entry field
        return self.zipcode_entry.get()

    def clear_data(self):
        # Delete the text entered in entry field
        self.zipcode_entry.delete(0, 'end')
