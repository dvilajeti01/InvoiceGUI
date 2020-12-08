import tkinter as tk
from tkinter import ttk


class EntriesList(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
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

    def load_entries(self, entries):
        # Index used to number items
        item_num = 1

        for entry in entries:
            # Append
            self.entries_lst.insert(
                '', 'end', text=item_num, values=entry)

            # Increment item number
            item_num = item_num + 1

    def append_entry(self, entry):
        # Next item number
        item_num = len(self.entries_lst.get_children()) + 1

        # Append entry to list
        self.entries_lst.insert(
            '', 'end', text=item_num, values=entry)

    def remove_entry(self, index):
        # Get the number of the item in the list != ID
        item_num = self.entries_lst.item(index, 'text')

        # Remove item from the list view
        self.entries_lst.delete(index)

        # Re-number the items
        for item in self.entries_lst.get_children():
            curr_item_num = int(self.entries_lst.item(item, 'text'))

            if curr_item_num > item_num:
                self.entries_lst.item(item, text=curr_item_num-1)

    def get_selection(self):
        # Fetch index of selected item
        selection = self.entries_lst.selection()

        # Return selection index & values if an item is selected
        if selection:
            return {
                'index': selection,
                'values': self.entries_lst.item(selection, 'values')
            }
        else:
            return None
