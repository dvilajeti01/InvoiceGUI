import tkinter as tk

BG_COLOR = "white"

BL_WIDTH = 100
BL_HEIGHT = 100


class CalendarBlock(tk.Frame):
    def __init__(self, parent, controller, block_id, row, col, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.block_id = block_id

        day = block_id.split("_")[2]

        # Defines minimum dimensions for the calendar
        self.rowconfigure(row, weight=1, minsize=BL_HEIGHT)
        self.columnconfigure(col, weight=1, minsize=BL_WIDTH)

        self["bg"] = BG_COLOR

        # Label display the day represented by calendar block
        self.date_lbl = tk.Label(
            self, text=day, fg="black", bg=BG_COLOR)
        self.date_lbl.grid(row=row, column=col, sticky="nw")

        # Label displays hours worked on the day represented by calendar block
        self.time_lbl = tk.Label(self, text="", bg=BG_COLOR)
        self.time_lbl.grid(row=row, column=col)
