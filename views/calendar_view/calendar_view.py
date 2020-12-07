import tkinter as tk

from views.calendar_view.calendar_menu import CalendarMenu
from views.calendar_view.calendar_section import CalendarSection
from views.calendar_view.main_header import MainHeader
from views.calendar_view.secondary_header import SecondaryHeader


class CalendarView(tk.Frame):
    def __init__(self, parent, controller, today, month, year, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        # Today's date
        self.today = today

        # Left Menu
        self.calendar_menu = CalendarMenu(self, controller)
        self.calendar_menu.pack(side=tk.LEFT, fill=tk.BOTH)

        # Main header that displays current month/year
        # Provides prev/next buttons to navigate calendar
        self.main_header = MainHeader(
            self, controller, month, year)
        self.main_header.pack(side=tk.TOP, fill=tk.BOTH)

        # Secondary header displays the days of the week
        self.secondary_header = SecondaryHeader(self, controller)
        self.secondary_header.pack(side=tk.TOP, fill=tk.BOTH)

        # Displays interactive days of the current month & year
        self.calendar_section = CalendarSection(
            self, controller, month, year)
        self.calendar_section.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def update_calendar_section(self, month, year):
        pass

    def update_main_header(self, month, year):
        pass

    def update_calendar_blocks(self, blocks_to_update, state):
        for block in blocks_to_update:
            self.calendar_section.blocks[block].set_state(state)
