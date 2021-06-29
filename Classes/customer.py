class Customer:
    def __init__(self, forename, surname, phone_number, email_address, postcode):
        self._forename = forename
        self._surname = surname
        self._phone_number = phone_number
        self._email_address = email_address
        self._postcode = postcode
        
    @property
    def forename(self):
        return self._forename

    @property
    def surname(self):
        return self._surname

    @property
    def phone_number(self):
        return self._phone_number

    @property
    def email_address(self):
        return self._email_address

    @property
    def postcode(self):
        return self._postcode

    def get_fullname(self):
        return f"{self.forename} {self.surname}"

    def __repr__(self):
        fullname = self.get_fullname().ljust(30)
        phone_number = str(self.phone_number).ljust(30)
        email_address = str(self.email_address).ljust(30)
        postcode = str(self.postcode)
        return f"{fullname}{phone_number}{email_address}{postcode}"