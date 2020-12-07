import tkinter as tk
from tkinter import ttk


class EntriesList(tk.Frame):
    def __init__(self, parent, controller, entries, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, parent, *args, **kwargs)

        self.entries_lst = ttk.Treeview(self)
        self.entries_lst.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.entries_lst['columns'] = [
            'Date', 'Description', 'Quantity', 'Rate']

        self.entries_lst.heading('#0', text='#')
        self.entries_lst.heading('Date', text='Date')
        self.entries_lst.heading('Description', text='Description')
        self.entries_lst.heading('Quantity', text='Quantity')
        self.entries_lst.heading('Rate', text='Rate')

        self.entries_lst.column('#0', width=30, stretch=tk.NO)
        self.entries_lst.column('Date', width=75, stretch=tk.NO)
        self.entries_lst.column('Description', width=400)
        self.entries_lst.column('Quantity', width=75, stretch=tk.NO)
        self.entries_lst.column('Rate', width=50, stretch=tk.NO)

        self.entries_scrl = tk.Scrollbar(self)
        self.entries_scrl.pack(side=tk.LEFT, fill=tk.BOTH)

        self.entries_lst.configure(yscrollcommand=self.entries_scrl.set)

        i = 1
        if entries is not None:
            for entry in entries:
                self.entries_lst.insert(
                    '', 'end', text=i, values=entry.to_tuple())
                i = i + 1
