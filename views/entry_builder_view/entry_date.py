import tkinter as tk


class EntryDate(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.date_lbl = tk.Label(self, text="Date")
        self.date_lbl.pack(side=tk.LEFT)

        self.date_entry = tk.Entry(self)
        self.date_entry.pack(side=tk.LEFT)
