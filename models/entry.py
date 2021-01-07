from json import JSONEncoder


class Entry:
    def __init__(self, date, description, quantity, rate, amount):

        self.date = date
        self.description = description
        self.quantity = float(quantity)
        self.rate = float(rate)
        self.amount = self.quantity * self.rate

    def to_list(self):
        return [self.date, self.description, self.quantity, self.rate, self.amount]

    @staticmethod
    def from_tuple(values):
        # Returns an entry object from Tuple values
        date, description, quantity, rate, amount = values

        return Entry(date, description, quantity, rate, amount)

    def __eq__(self, other):
        # Compare to Entry objects
        # This approach looks better than a super long if statement
        this_values = self.to_list()
        other_values = other.to_list()

        if this_values == other_values:
            return True
        else:
            return False

    def __iter__(self):
        # Returns the object as an iterable
        return iter(self.to_list())


class EntryEncoder(JSONEncoder):
    def default(self, o):
        return {
            'Date': o.date,
            'Description': o.description,
            'Quantity': o.quantity,
            'Rate': o.rate,
            'Amount': o.amount
        }
