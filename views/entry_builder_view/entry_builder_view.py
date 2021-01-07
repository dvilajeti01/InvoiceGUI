import tkinter as tk

from views.entry_builder_view.entry_desc import EntryDesc
from views.entry_builder_view.entry_date import EntryDate
from views.entry_builder_view.entry_qnty import EntryQnty
from views.entry_builder_view.entry_rate import EntryRate
from views.entry_builder_view.entry_footer import EntryFooter


class EntryBuilderView(tk.Toplevel):
    def __init__(self, parent, controller, date, *args, **kwargs):
        # Call parent init
        tk.Toplevel.__init__(self, parent, *args, **kwargs)

        self.date_entry = EntryDate(self, controller, date)
        self.date_entry.pack(side=tk.TOP, anchor='w')

        self.desc_entry = EntryDesc(self, controller)
        self.desc_entry.pack(side=tk.TOP, anchor='w')

        self.qnty_entry = EntryQnty(self, controller)
        self.qnty_entry.pack(side=tk.TOP, anchor='w')

        self.rate_entry = EntryRate(self, controller)
        self.rate_entry.pack(side=tk.TOP, anchor='w')

        self.entry_footer = EntryFooter(self, controller)
        self.entry_footer.pack(side=tk.TOP)

    def get_entries(self):
        # Fetch the data from each entry field
        date = self.date_entry.get_data()
        desc = self.desc_entry.get_data()
        qnty = float(self.qnty_entry.get_data())
        rate = float(self.rate_entry.get_data())
        amount = qnty * rate

        # Return data in form of a tuple
        return (date, desc, qnty, rate, amount)

    def clear_entries(self):
        # Clear text from each entry field

        self.date_entry.clear_data()
        self.desc_entry.clear_data()
        self.qnty_entry.clear_data()
        self.rate_entry.clear_data()
