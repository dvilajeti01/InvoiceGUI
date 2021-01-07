import tkinter as tk


class DateEntry(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.date_lbl = tk.Label(self, text='Due Date')
        self.date_lbl.pack(side=tk.LEFT)

        self.date_entry = tk.Entry(self, width=10)
        self.date_entry.insert(0, 'mm/dd/yyyy')
        self.date_entry.pack(side=tk.LEFT)

    def get_data(self):
        # Return the text entered in entry field
        return self.date_entry.get()

    def clear_data(self):
        # Delete the text entered in entry field
        self.date_entry.delete(0, 'end')
