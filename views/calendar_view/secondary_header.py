import tkinter as tk

DAYS_OF_THE_WEEK = ['Su', 'Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa']


class SecondaryHeader(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.parent = parent
        self.controller = controller

        for day in DAYS_OF_THE_WEEK:
            day_lbl = tk.Label(self,
                               text=day)
            day_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
