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

        self.entries_list = EntriesList(self, controller)
        self.entries_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        self.load_entries(entries)

        self.entries_menu = EntriesMenu(self, controller)
        self.entries_menu.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def load_entries(self, entries):
        # Load entries to list view
        self.entries_list.load_entries(entries)

    def append_entry(self, entry):
        # Append entry to entries list
        self.entries_list.append_entry(entry)

    def remove_entry(self, index):
        # Remove entry from entries list
        self.entries_list.remove_entry(index)

    def get_selected_entry(self):
        return self.entries_list.get_selection()
