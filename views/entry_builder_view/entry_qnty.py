import tkinter as tk


class EntryQnty(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.qnty_lbl = tk.Label(self, text='Quantity')
        self.qnty_lbl.pack(side=tk.LEFT)

        self.qnty_entry = tk.Entry(self)
        self.qnty_entry.pack(side=tk.LEFT)

    def get_data(self):
        # Return the text entered in entry field
        return self.qnty_entry.get()

    def clear_data(self):
        # Delete the text entered in entry field
        self.qnty_entry.delete(0, 'end')
