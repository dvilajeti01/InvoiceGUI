import tkinter as tk

from views.settings_view.name_entry import NameEntry
from views.settings_view.address_entry import AddressEntry
from views.settings_view.city_entry import CityEntry
from views.settings_view.state_entry import StateEntry
from views.settings_view.zipcode_entry import ZipCodeEntry
from views.settings_view.settings_footer import SettingsFooter


class SettingsView(tk.Frame):
    def __init__(self, parent, controller, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)

        header_font = ('Helvetica', 20, 'bold')

        # To Section
        self.to_header = tk.Label(self, text='To', font=header_font)
        self.to_header.pack(side=tk.TOP, anchor='w')

        # Name
        self.to_name = NameEntry(self, controller)
        self.to_name.pack(side=tk.TOP, anchor='w')

        # Address
        self.to_address = AddressEntry(self, controller)
        self.to_address.pack(side=tk.TOP, anchor='w')

        # City
        self.to_city = CityEntry(self, controller)
        self.to_city.pack(side=tk.TOP, anchor='w')

        # State
        self.to_state = StateEntry(self, controller)
        self.to_state.pack(side=tk.TOP, anchor='w')

        # Zipcode
        self.to_zipcode = ZipCodeEntry(self, controller)
        self.to_zipcode.pack(side=tk.TOP, anchor='w')

        # From Section
        self.from_header = tk.Label(self, text='From', font=header_font)
        self.from_header.pack(side=tk.TOP, anchor='w')

        # Name
        self.from_name = NameEntry(self, controller)
        self.from_name.pack(side=tk.TOP, anchor='w')

        # Address
        self.from_address = AddressEntry(self, controller)
        self.from_address.pack(side=tk.TOP, anchor='w')

        # City
        self.from_city = CityEntry(self, controller)
        self.from_city.pack(side=tk.TOP, anchor='w')

        # State
        self.from_state = StateEntry(self, controller)
        self.from_state.pack(side=tk.TOP, anchor='w')

        # Zipcode
        self.from_zipcode = ZipCodeEntry(self, controller)
        self.from_zipcode.pack(side=tk.TOP, anchor='w')

        # Footer
        self.settings_footer = SettingsFooter(self, controller)
        self.settings_footer.pack(side=tk.TOP)

    def set_sender(self, sender):
        # Set sender data in respective fields
        self.from_name.set_data(sender['name'])
        self.from_address.set_data(sender['address'])
        self.from_city.set_data(sender['city'])
        self.from_state.set_data(sender['state'])
        self.from_zipcode.set_data(sender['zipcode'])

    def set_recipient(self, recipient):
        # Set recipient data in respective fields
        self.to_name.set_data(recipient['name'])
        self.to_address.set_data(recipient['address'])
        self.to_city.set_data(recipient['city'])
        self.to_state.set_data(recipient['state'])
        self.to_zipcode.set_data(recipient['zipcode'])

    def get_recipient(self):
        return {
            'name': self.to_name.get_data(),
            'address': self.to_address.get_data(),
            'city': self.to_city.get_data(),
            'state': self.to_state.get_data(),
            'zipcode': self.to_zipcode.get_data()
        }

    def get_sender(self):
        return {
            'name': self.from_name.get_data(),
            'address': self.from_address.get_data(),
            'city': self.from_city.get_data(),
            'state': self.from_state.get_data(),
            'zipcode': self.from_zipcode.get_data()
        }
