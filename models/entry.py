class Entry:
    def __init__(self, date, description, quantity, rate):

        self.date = date
        self.description = description
        self.quantity = quantity
        self.rate = rate

    def to_tuple(self):

        return (self.date, self.description, self.quantity, self.rate)
