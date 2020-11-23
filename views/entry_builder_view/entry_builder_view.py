import tkinter as tk

from views.entry_builder_view.entry_desc import EntryDesc
from views.entry_builder_view.entry_date import EntryDate
from views.entry_builder_view.entry_qnty import EntryQnty
from views.entry_builder_view.entry_rate import EntryRate
from views.entry_builder_view.entry_footer import EntryFooter


class EntryBuilderView(tk.Toplevel):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Toplevel.__init__(self, parent, *args, **kwargs)

        self.date_entry = EntryDate(self, controller)
        self.date_entry.pack(side=tk.TOP, anchor="w")

        self.dsc_entry = EntryDesc(self, controller)
        self.dsc_entry.pack(side=tk.TOP, anchor="w")

        self.qnty_entry = EntryQnty(self, controller)
        self.qnty_entry.pack(side=tk.TOP, anchor="w")

        self.rate_entry = EntryRate(self, controller)
        self.rate_entry.pack(side=tk.TOP, anchor="w")

        self.entry_footer = EntryFooter(self, controller)
        self.entry_footer.pack(side=tk.TOP)