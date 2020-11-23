import tkinter as tk
import calendar as cl


class MainHeader(tk.Frame):
    def __init__(self, parent, controller, month, year, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # Header displays month,year being currently displayed
        header_font = ("Helvetica", 20, "bold")
        self.header_lbl = tk.Label(
            self, text=f"{cl.month_name[month]}, {year}", font=header_font)
        self.header_lbl.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Displays previous month
        self.prev_month_btn = tk.Button(
            self, text="<", width=5)
        self.prev_month_btn.pack(side=tk.LEFT, fill=tk.BOTH)
        self.prev_month_btn.bind("<Button-1>", controller.prev_month)

        # Displays next month
        self.next_month_btn = tk.Button(
            self, text=">", width=5)
        self.next_month_btn.pack(side=tk.LEFT, fill=tk.BOTH)
        self.next_month_btn.bind("<Button-1>", controller.next_month)
