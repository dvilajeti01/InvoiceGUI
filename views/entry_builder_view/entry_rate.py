import tkinter as tk


class EntryRate(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.rate_lbl = tk.Label(self, text="Rate")
        self.rate_lbl.pack(side=tk.LEFT)

        self.rate_entry = tk.Entry(self)
        self.rate_entry.pack(side=tk.LEFT)
