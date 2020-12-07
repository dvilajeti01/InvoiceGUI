import tkinter as tk
import calendar as cl

from views.calendar_view.calendar_block import CalendarBlock

# Start on Sunday as the first day of the week
FIRST_WEEK_DAY = 6

# Rows and columns for the calendar section
ROWS = 6  # Weeks
COLUMNS = 7  # Days of the week


class CalendarSection(tk.Frame):
    def __init__(self, parent, controller, month, year, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # Month and year to be displayed
        month = month
        year = year

        # Calendar manager
        calendar_manager = cl.Calendar(firstweekday=FIRST_WEEK_DAY)

        # Generate all dates in a given month and year
        date_generator = calendar_manager.itermonthdays3(
            year, month)

        self.blocks = {}

        for i in range(ROWS):
            for j in range(COLUMNS):

                # Allows the frame that contains calendar to expand proportionally
                self.rowconfigure(i, weight=1)
                self.columnconfigure(j, weight=1)

                try:
                    block_year, block_month, block_day = next(
                        date_generator)
                except StopIteration:
                    if block_day == 28 or block_day == 29:
                        block_day = 1
                        block_month = block_month + 1
                    else:
                        block_day = block_day + 1
                finally:
                    # Each block is to be identified by a unique ID
                    # The ID is made up by the year,month, and day
                    # delimited by '_'
                    block_id = f"{block_month}_{block_day}_{block_year}"

                    calendar_block = CalendarBlock(
                        self,
                        controller,
                        block_id=block_id,
                        row=i,
                        col=j,
                        relief=tk.RIDGE,
                        borderwidth=1)
                    calendar_block.grid(row=i, column=j, sticky='nsew')

                    # CalendarBlock frame bindings
                    calendar_block.bind('<Enter>', controller.hover_in)
                    calendar_block.bind('<Leave>', controller.hover_out)
                    calendar_block.bind('<Double-Button-1>',
                                        controller.enter_entries_view)

                    self.blocks[block_id] = calendar_block

    def get_calendar_blocks(self):
        return self.blocks
