import tkinter as tk


class StateEntry(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.state_lbl = tk.Label(self, text='State')
        self.state_lbl.pack(side=tk.LEFT, anchor='w')

        self.state_entry = tk.Entry(self)
        self.state_entry.pack(side=tk.LEFT)

    def set_data(self, data):
        self.state_entry.insert(0, data)

    def get_data(self):
        # Return the text entered in entry field
        return self.state_entry.get()

    def clear_data(self):
        # Delete the text entered in entry field
        self.state_entry.delete(0, 'end')
