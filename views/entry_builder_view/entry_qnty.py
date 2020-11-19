import tkinter as tk


class EntryQnty(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.qnty_lbl = tk.Label(self, text="Quantity")
        self.qnty_lbl.pack(side=tk.LEFT)

        self.qnty_entry = tk.Entry(self)
        self.qnty_entry.pack(side=tk.LEFT)
