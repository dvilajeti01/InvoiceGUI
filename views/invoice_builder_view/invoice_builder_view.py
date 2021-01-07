import tkinter as tk

from views.invoice_builder_view.date_entry import DateEntry
from views.invoice_builder_view.file_entry import FileEntry


class InvoiceBuilderView(tk.Toplevel):
    def __init__(self, parent, controller, *args, **kwargs):
        # Call parent init
        tk.Toplevel.__init__(self, parent, *args, **kwargs)

        self.date_entry = DateEntry(self, controller)
        self.date_entry.pack(side=tk.TOP, anchor='w')

        self.file_entry = FileEntry(self, controller)
        self.file_entry.pack(side=tk.TOP, anchor='w')

        # Button to generate invoice
        self.generate_btn = tk.Button(
            self, text='Generate', relief=tk.RAISED, fg='green')
        self.generate_btn.pack(side=tk.TOP, fill=tk.BOTH)

        self.generate_btn.bind('<Button-1>', controller.generate_invoice)

    def get_due_date(self):
        return self.date_entry.get_data()

    def get_file_name(self):
        return self.file_entry.get_data()
