import tkinter as tk

BG_COLOR = "#FFFFFF"

BL_WIDTH = 100
BL_HEIGHT = 100


class CalendarBlock(tk.Frame):
    def __init__(self, parent, controller, block_id, row, col, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.block_id = block_id

        day = block_id.split("_")[1]

        # Defines minimum dimensions for the calendar
        self.rowconfigure(row, weight=1, minsize=BL_HEIGHT)
        self.columnconfigure(col, weight=1, minsize=BL_WIDTH)

        self["bg"] = BG_COLOR

        # Label display the day represented by calendar block
        self.date_lbl = tk.Label(
            self, text=day, fg="black", bg=BG_COLOR)
        self.date_lbl.grid(row=row, column=col, sticky="nw")

        # Label indicates if there are any entries listed for this date
        self.active_lbl = tk.Label(self, text="", bg=BG_COLOR)
        self.active_lbl.grid(row=row, column=col)

    def change_background(self, color):

        # Set background color of the frame
        self['bg'] = color

        # Set the background color for all child frames
        for child in self.winfo_children():
            child['bg'] = color

    def set_state(self, active):

        if active:
            # If active place a green * in the middle of the frame
            # this is used to indicate that an entrie exists for this
            # given block

            self.active_lbl['fg'] = '#00FF00'
            self.active_lbl['text'] = '*'
        else:
            # Else revert back to normal

            self.active_lbl['fg'] = '#FFFFFF'
            self.active_lbl['text'] = ''
