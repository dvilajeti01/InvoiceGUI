import tkinter as tk

TITLE_FONT = ('Helvetica', 20, 'bold')
HEADER_TITLE = 'Entries'


class EntriesHeader(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.title_lbl = tk.Label(self, text=HEADER_TITLE, font=TITLE_FONT)
        self.title_lbl.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
