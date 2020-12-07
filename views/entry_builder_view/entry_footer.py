import tkinter as tk


class EntryFooter(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.add_btn = tk.Button(self, text='Add')
        self.add_btn.pack(side=tk.TOP, fill=tk.BOTH)

        self.add_btn.bind('<Button-1>', controller.add_entry)
