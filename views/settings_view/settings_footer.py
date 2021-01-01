import tkinter as tk


class SettingsFooter(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # Save Button
        self.save_btn = tk.Button(self, text='Save')
        self.save_btn.pack(side=tk.TOP, fill=tk.BOTH)

        self.save_btn.bind('<Button-1>', controller.save_settings)

        # Done Button
        self.done_btn = tk.Button(self, text='Done')
        self.done_btn.pack(side=tk.TOP, fill=tk.BOTH)

        self.done_btn.bind('<Button-1>', controller.return_to_calendar)
