import tkinter as tk

WIDTH = 50


class EntryDesc(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.desc_lbl = tk.Label(self, text='Description')
        self.desc_lbl.pack(side=tk.LEFT, anchor='w')

        self.desc_entry = tk.Entry(self, width=WIDTH)
        self.desc_entry.pack(side=tk.LEFT)

    def get_data(self):
        # Return the text entered in entry field
        return self.desc_entry.get()

    def clear_data(self):
        # Delete the text entered in entry field
        self.desc_entry.delete(0, 'end')
