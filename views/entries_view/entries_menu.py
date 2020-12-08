import tkinter as tk


class EntriesMenu(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.new_btn = tk.Button(
            self, text='New')
        self.new_btn.pack(side=tk.TOP, fill=tk.X)
        self.new_btn.bind('<Button-1>', controller.new_entry)

        self.delete_btn = tk.Button(
            self, text='Delete')
        self.delete_btn.pack(side=tk.TOP, fill=tk.X)
        self.delete_btn.bind('<Button-1>', controller.delete_entry)

        self.done_btn = tk.Button(self, text='Done')
        self.done_btn.pack(side=tk.TOP, fill=tk.X)
        self.done_btn.bind('<Button-1>', controller.return_to_calendar)
