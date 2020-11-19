import tkinter as tk

WIDTH = 50


class EntryDesc(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.desc_lbl = tk.Label(self, text="Description")
        self.desc_lbl.pack(side=tk.LEFT)

        self.desc_entry = tk.Entry(self, width=WIDTH)
        self.desc_entry.pack(side=tk.LEFT)
