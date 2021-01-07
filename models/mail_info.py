class MailInfo:
    def __init__(self, name='', address='', city='', state='', zipcode=''):

        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def get_info(self):
        return {
            'name': self.name,
            'address': self.address,
            'city': self.city,
            'state': self.state,
            'zipcode': self.zipcode
        }

    @staticmethod
    def from_dict(dict):
        return MailInfo(dict['name'],
                        dict['address'],
                        dict['city'],
                        dict['state'],
                        dict['zipcode'])
