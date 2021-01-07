import os
import json

import tkinter as tk
from datetime import datetime
import calendar as cl
import pandas as pd

from views.calendar_view.calendar_view import CalendarView
from views.entries_view.entries_view import EntriesView
from views.entry_builder_view.entry_builder_view import EntryBuilderView
from views.settings_view.settings_view import SettingsView

from models.entry import Entry, EntryEncoder
from models.invoice import Invoice
from models.mail_info import MailInfo


class InvoiceApp(tk.Frame):
    def __init__(self, root, *args, **kwargs):
        # Call parent init
        tk.Frame.__init__(self, root, *args, **kwargs)

        # Today's date
        self.today = datetime.today()

        self.month = self.today.month
        self.year = self.today.year

        # Initialize an empty invoice
        self.invoice = Invoice()

        # CalendarView displaying todays date
        self.calendar_view = CalendarView(
            self, self, self.today, self.today.month, self.today.year)
        self.current_view = self.calendar_view

        self.current_view.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.entries_view = None
        self.data_entry = None
        self.settings_view = None

        # Load last used settings if any
        self.read_settings()

        self.current_block = None

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

        # Decrements year when going from January to December
        if self.month < 1:
            self.month = 12
            self.year = self.year - 1

        self.calendar_view.update_idletasks()

        # Update calendar to display next month's days
        self.calendar_view.update_calendar(self.month, self.year)

        # Mark blocks with entries as active
        active_dates = self.get_active_dates()
        self.calendar_view.update_calendar_blocks(active_dates, True)

    def next_month(self, event):
        self.month = self.month + 1

        # Increments year when going from December to January
        if self.month > 12:
            self.month = 1
            self.year = self.year + 1

        self.calendar_view.update_idletasks()

        # Update calendar to display next month's days
        self.calendar_view.update_calendar(self.month, self.year)

        # Mark blocks with entries as active
        active_dates = self.get_active_dates()
        self.calendar_view.update_calendar_blocks(active_dates, True)

    def new_entry(self, event):
        # Convert block id into a valid date
        date = self.current_block.replace('_', '/')

        # Build pop up view to enter entry data
        self.data_entry = EntryBuilderView(self, self, date)

        # Disable parent view while pop up is visible
        self.data_entry.wait_visibility()
        self.data_entry.grab_set()

    def add_entry(self, event):
        # Fetch values entered in entry fields
        entry_data = self.data_entry.get_entries()

        # Initialize Entry object from values
        entry = Entry.from_tuple(entry_data)

        # Append entry to invoice
        self.invoice.append_entry(entry)

        # Append entry to list view
        self.entries_view.append_entry(entry.to_list())

        # Clear text from entries
        self.data_entry.clear_entries()

    def delete_entry(self, event):
        # Get selected item from list
        selection = self.entries_view.get_selected_entry()

        if selection is not None:
            # Initialize entry from selection values
            entry = Entry.from_tuple(selection['values'])

            # Remove entry form invoice
            self.invoice.remove_entry(entry)

            # Remove entry from list view
            self.entries_view.remove_entry(selection['index'])

    def enter_entries_view(self, event):

        block_id = event.widget.block_id
        self.current_block = block_id

        # Create entries view
        self.entries_view = EntriesView(self, self, [])

        entries_to_load = self.invoice.get_entries(self.current_block)

        # Load entries into view
        for entry in entries_to_load:
            self.entries_view.append_entry(entry)

        # Destroy current calendar view
        self.current_view.destroy()
        self.current_view = None

        # Display entries view
        self.current_view = self.entries_view
        self.current_view.pack(
            side=tk.TOP, fill=tk.BOTH, expand=True)

    def return_to_calendar(self, event):

        self.current_block = None

        # Create calendar view
        self.calendar_view = CalendarView(
            self, self, self.today, self.month, self.year)

        # Destroy current displayed view
        self.current_view.destroy()
        self.entries_view = None

        # Display calendar view
        self.current_view = self.calendar_view
        self.current_view.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        active_dates = self.get_active_dates()
        self.calendar_view.update_calendar_blocks(active_dates, True)

    def generate_invoice(self, event):
        self.invoice.generate_invoice(
            file_name='/mnt/c/Users/danie/OneDrive/Desktop/invoice')

    def enter_settings_view(self, event):
        # Create settings view
        self.settings_view = SettingsView(self, self)

        # Destroy current calendar view
        self.calendar_view.destroy()
        self.calendar_view = None

        # Display entries view
        self. current_view = self.settings_view

        # Load last used settings if any
        self.read_settings()

        self.current_view.pack(
            side=tk.TOP, fill=tk.BOTH, expand=True)

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
                date = f"{month}/{day}/{year}"

                if self.invoice.has_date(date):
                    dates.append(date)

        return dates

    def save_settings(self, event):

        # Get sender/recipient info
        sender = self.settings_view.get_sender()
        recipient = self.settings_view.get_recipient()

        # Build mailing info dict to parse as json
        mail_info = {
            'sender': sender,
            'recipient': recipient
        }

        # Write to json file to retrieve later
        with open('mail_info.json', 'w') as file:
            json.dump(mail_info, file, indent=4)

        # Set mail info for invoice
        self.invoice.sender = MailInfo.from_dict(sender)
        self.invoice.recipient = MailInfo.from_dict(recipient)

    def read_settings(self):

        if os.path.exists('./mail_info.json'):
            # read from json data
            with open('mail_info.json') as file:
                mail_info = json.load(file)

                if self.settings_view is not None:

                    self.settings_view.set_sender(mail_info['sender'])
                    self.settings_view.set_recipient(mail_info['recipient'])

                # Set mail info for invoice
                self.invoice.sender = MailInfo.from_dict(mail_info['sender'])
                self.invoice.recipient = MailInfo.from_dict(
                    mail_info['recipient'])
        else:
            print('no settings available')
