import tkinter as tk
from datetime import datetime
import calendar as cl
import pandas as pd
import json

from views.calendar_view.calendar_view import CalendarView
from views.entries_view.entries_view import EntriesView
from views.entry_builder_view.entry_builder_view import EntryBuilderView

from models.entry import Entry, EntryEncoder


class InvoiceApp(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, root, *args, **kwargs)

        # Today's date
        self.today = datetime.today()

        self.month = self.today.month
        self.year = self.today.year

        self.current_block = None

        self.entries = {}

        # CalendarView displaying todays date
        self.calendar_view = CalendarView(
            self, self, self.today, self.today.month, self.today.year)
        self.calendar_view.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for block in self.calendar_view.calendar_section.winfo_children():
            try:
                if len(self.entries[block.block_id]) > 0:
                    block.active_lbl["fg"] = "Green"
                    block.active_lbl["text"] = "*"
            except KeyError:
                pass

        self.entries_view = None
        self.data_entry = None

    def hover_in(self, event):
        # Changes background color of calendar block to
        # notify users they are pointing to calendar block

        event.widget["bg"] = "#D7DBDD"

        for child in event.widget.winfo_children():
            child["bg"] = "#D7DBDD"

    def hover_out(self, event):
        # Reverts background color of calendar block to
        # notify users they are no longer pointing to calendar block

        event.widget["bg"] = "white"

        for child in event.widget.winfo_children():
            child["bg"] = "white"

    def prev_month(self, event):
        self.month = self.month - 1

        if self.month < 1:
            self.month = 12
            self.year = self.year - 1

        # Build updated calendar view
        new_cal_view = CalendarView(
            self, self, self.today, self.month, self.year)

        self.calendar_view.destroy()

        self.calendar_view = new_cal_view
        self.calendar_view.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for block in self.calendar_view.calendar_section.winfo_children():
            try:
                if len(self.entries[block.block_id]) > 0:
                    block.active_lbl["fg"] = "Green"
                    block.active_lbl["text"] = "*"
            except KeyError:
                pass

    def next_month(self, event):
        self.month = self.month + 1

        if self.month > 12:
            self.month = 1
            self.year = self.year + 1

        # Build updated calendar section
        new_cal_view = CalendarView(
            self, self, self.today, self.month, self.year)

        self.calendar_view.destroy()

        self.calendar_view = new_cal_view
        self.calendar_view.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        for block in self.calendar_view.calendar_section.winfo_children():
            try:
                if len(self.entries[block.block_id]) > 0:
                    block.active_lbl["fg"] = "Green"
                    block.active_lbl["text"] = "*"
            except KeyError:
                pass

    def new_entry(self, event):

        date = self.current_block.replace('_', '/')

        self.data_entry = EntryBuilderView(self, self, date)
        self.data_entry.wait_visibility()
        self.data_entry.grab_set()

    def add_entry(self, event):
        date = self.data_entry.date_entry.date_entry.get()
        desc = self.data_entry.dsc_entry.desc_entry.get()
        qnty = self.data_entry.qnty_entry.qnty_entry.get()
        rate = self.data_entry.rate_entry.rate_entry.get()

        entry = Entry(date, desc, qnty, rate)
        item_num = len(
            self.entries_view.entries_list.entries_lst.get_children())
        try:
            self.entries[self.current_block]
        except KeyError:
            self.entries[self.current_block] = []

        self.entries[self.current_block].append(entry)
        self.entries_view.entries_list.entries_lst.insert(
            '', 'end', text=item_num+1, values=(entry.to_tuple()))

        self.data_entry.date_entry.date_entry.delete(0, "end")
        self.data_entry.dsc_entry.desc_entry.delete(0, "end")
        self.data_entry.qnty_entry.qnty_entry.delete(0, "end")
        self.data_entry.rate_entry.rate_entry.delete(0, "end")

    def delete_entry(self, event):
        item = self.entries_view.entries_list.entries_lst.selection()

        if item != ():
            entry_values = self.entries_view.entries_list.entries_lst.item(
                item, "values")

            entry = Entry.from_tuple(entry_values)
            self.entries[self.current_block].remove(entry)
            self.entries_view.entries_list.entries_lst.delete(item)
        else:
            print("Nothing to Delete!")

    def enter_entries_view(self, event):

        block_id = event.widget.block_id
        self.current_block = block_id

        # Create entries view
        try:
            self.entries_view = EntriesView(self, self, self.entries[block_id])
        except KeyError:
            self.entries_view = EntriesView(self, self, [])

        # Destroy current calendar view
        self.calendar_view.destroy()
        self.calendar_view = None

        # Display entries view
        self.entries_view.pack(
            side=tk.TOP, fill=tk.BOTH, expand=True)

    def return_to_calendar(self, event):

        self.current_block = None
        # Create calendar view
        self.calendar_view = CalendarView(
            self, self, self.today, self.month, self.year)

        for block in self.calendar_view.calendar_section.winfo_children():
            try:
                if len(self.entries[block.block_id]) > 0:
                    block.active_lbl["fg"] = "Green"
                    block.active_lbl["text"] = "*"
            except KeyError:
                pass

        # Destroy current entries view
        self.entries_view.destroy()
        self.entries_view = None

        # Display calendar view
        self.calendar_view.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

    def generate_invoice(self, event):
        invoice = []

        for block in self.entries:
            for entry in self.entries[block]:
                invoice.append(entry)

        if invoice:
            invoiceJOSNData = json.dumps(invoice, indent=4, cls=EntryEncoder)
            print(invoiceJOSNData)

            invoice_frame = pd.read_json(invoiceJOSNData)

            invoice_frame_sorted = invoice_frame.sort_values(
                by='date', ascending=True)

            invoice_frame_sorted.loc[:, "amount"] = invoice_frame_sorted["quantity"] * \
                invoice_frame_sorted["rate"]

            columns_to_total = ["quantity", "amount"]
            invoice_frame_sorted.loc["Total", :] = invoice_frame_sorted[columns_to_total].sum(
                axis=0, numeric_only=True)
            invoice_frame_sorted.fillna("")

            print(invoice_frame_sorted)
            invoice_frame_sorted.to_csv(
                "/mnt/c/Users/danie/Desktop/invoice.csv")
        else:
            print("No entries to generate invoice :(")
