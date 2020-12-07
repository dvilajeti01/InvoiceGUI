from json import JSONEncoder


class Entry:
    def __init__(self, date, description, quantity, rate):

        self.date = date
        self.description = description
        self.quantity = quantity
        self.rate = rate

    def to_dict(self):

        return {
            'Date': self.date,
            'Description': self.description,
            'Quantity': self.quantity,
            'Rate': self.rate
        }

    def to_tuple(self):

        return (self.date, self.description, self.quantity, self.rate)

    @staticmethod
    def from_tuple(values):
        date, description, quantity, rate = values

        return Entry(date, description, quantity, rate)

    def __eq__(self, other):
        this_values = self.to_tuple()
        other_values = other.to_tuple()

        if this_values == other_values:
            return True
        else:
            return False


class EntryEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__
