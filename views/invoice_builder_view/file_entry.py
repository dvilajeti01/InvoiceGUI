import tkinter as tk

WIDTH = 50


class FileEntry(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.file_lbl = tk.Label(self, text='File Name')
        self.file_lbl.pack(side=tk.LEFT, anchor='w')

        self.file_entry = tk.Entry(self, width=WIDTH)
        self.file_entry.pack(side=tk.LEFT)

    def get_data(self):
        # Return the text entered in entry field
        return self.file_entry.get()

    def clear_data(self):
        # Delete the text entered in entry field
        self.file_entry.delete(0, 'end')
