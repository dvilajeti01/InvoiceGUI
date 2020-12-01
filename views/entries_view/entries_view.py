import tkinter as tk

from views.entries_view.entries_header import EntriesHeader
from views.entries_view.entries_menu import EntriesMenu
from views.entries_view.entries_list import EntriesList


class EntriesView(tk.Frame):
    def __init__(self, parent, controller, entries, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.entries_header = EntriesHeader(self, controller)
        self.entries_header.pack(side=tk.TOP, fill=tk.BOTH)

        self.entries_list = EntriesList(self, controller, entries)
        self.entries_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.entries_menu = EntriesMenu(self, controller)
        self.entries_menu.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
