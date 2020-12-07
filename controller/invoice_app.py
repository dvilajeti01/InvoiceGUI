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

        active_dates = self.get_active_dates()
        self.calendar_view.update_calendar_blocks(active_dates, True)

        self.entries_view = None
        self.data_entry = None

    def hover_in(self, event):
        # Changes background color of calendar block to
        # notify users they are pointing to calendar block

        event.widget.change_background('#D7DBDD')

    def hover_out(self, event):
        # Reverts background color of calendar block to
        # notify users they are no longer pointing to calendar block

        event.widget.change_background('#FFFFFF')

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

        active_dates = self.get_active_dates()
        self.calendar_view.update_calendar_blocks(active_dates, True)

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

        active_dates = self.get_active_dates()
        self.calendar_view.update_calendar_blocks(active_dates, True)

    def new_entry(self, event):

        date = self.current_block.replace('_', '/')

        self.data_entry = EntryBuilderView(self, self, date)
        self.data_entry.wait_visibility()
        self.data_entry.grab_set()

    def add_entry(self, event):
        # Fetch values entered in entry fields
        entry_data = self.data_entry.get_entries()

        # Initialize Entry object from values
        entry = Entry.from_tuple(entry_data)

        # Get curr length of the list
        item_num = len(
            self.entries_view.entries_list.entries_lst.get_children())

        # Initialize list of entries for date in dict
        if self.current_block not in self.entries:
            self.entries[self.current_block] = []

        # Append entry to dict
        self.entries[self.current_block].append(entry)

        # Append entry with incremented item_num to list view
        self.entries_view.entries_list.entries_lst.insert(
            '', 'end', text=item_num+1, values=(entry.to_tuple()))

        # Clear text from entries
        self.data_entry.clear_entries()

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

        # Destroy current entries view
        self.entries_view.destroy()
        self.entries_view = None

        # Display calendar view
        self.calendar_view.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        active_dates = self.get_active_dates()
        self.calendar_view.update_calendar_blocks(active_dates, True)

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

    def get_active_dates(self):

        dates = []

        # Calendar manager
        calendar_manager = cl.Calendar(firstweekday=6)

        # Generate all dates in a given month and year
        date_generator = calendar_manager.itermonthdays3(
            self.year, self.month)

        for i in range(42):
            try:
                year, month, day = next(date_generator)
            except StopIteration:
                if day == 28 or day == 29:
                    day = 1
                    month = month + 1
                else:
                    day = day + 1
            finally:
                date = f"{month}_{day}_{year}"

                if date in self.entries:
                    dates.append(date)

        return dates
