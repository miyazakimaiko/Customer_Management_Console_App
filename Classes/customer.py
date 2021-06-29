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
        return f"(Fullname: {self.forename}, {self.surname} Phone Number: {self.phone_number} Email Address:{self.email_address} Postcode: {self.postcode})"