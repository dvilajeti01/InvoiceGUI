import tkinter as tk


class CalendarMenu(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # Button to clear progress
        self.clear_btn = tk.Button(
            self, text='Clear')
        self.clear_btn.pack(side=tk.TOP, fill=tk.X)
        self.clear_btn.bind('<Button-1>', controller.clear_entries)

        # Button to generate invoice
        self.generate_btn = tk.Button(
            self, text='Generate', relief=tk.RAISED, fg='green')
        self.generate_btn.pack(side=tk.TOP, fill=tk.X)
        self.generate_btn.bind('<Button-1>', controller.enter_invoice_builder)

        # Button to set invoice generating settings
        self.settings_btn = tk.Button(
            self, text='Settings', relief=tk.RAISED)
        self.settings_btn.pack(
            side=tk.BOTTOM, fill=tk.X)

        self.settings_btn.bind('<Button-1>', controller.enter_settings_view)
