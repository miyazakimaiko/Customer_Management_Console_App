class Customer:

    next_customer_id = 1

    def __init__(self, forename, surname, phone_number, email_address, postcode):
        self._forename = forename
        self._surname = surname
        self._phone_number = phone_number
        self._email_address = email_address
        self._postcode = postcode
        self._id = self.next_customer_id

        Customer.next_customer_id += 1
        
    @property
    def cust_id(self):
        return self._id

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
        cust_id = str(self.cust_id).ljust(10)
        fullname = self.get_fullname().ljust(30)
        phone_number = str(self.phone_number).ljust(30)
        email_address = str(self.email_address).ljust(30)
        postcode = str(self.postcode)
        return f"{cust_id}{fullname}{phone_number}{email_address}{postcode}"