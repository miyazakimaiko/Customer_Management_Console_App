from .utils import Utils
from .customer import Customer

class MainMenu:

    def display_options(self):
        print()
        print("Main Menu")
        print()
        print("______Options_____")
        print("")
        print("1. View existing Customers")
        print("2. Add Customer")
        print("3. Exit")


    def get_selection_via_input(self):
        selection = input('Please enter a number (1 - 3): ')

        try:
            selection = int(selection)
        except:
            print('Wrong format. Please enter a digit.')
            selection = self.get_selection_via_input()

        if selection > 3 or selection < 1:
            print('Selection out of range. Please enter a digit between 1 and 3.')
            selection = self.get_selection_via_input()

        return selection


    def view_customers(self, customers):
        print()
        print('ID: '.ljust(10) + 'Name: '.ljust(30) + 'Phone Number: '.ljust(30) + 'Email Address: '.ljust(30) + 'Postcode: '.ljust(30))
        print(''.ljust(120, '-'))

        for customer in customers.group:
            print(customer)

        print()


    def get_new_customer_phone_number_via_input(self, customers):
        phone_number = input('Please enter phone_number: ')
        
        for customer in customers.group:
            if phone_number == customer.phone_number:
                print('This phone number is already registered. Please try with different phone number.')
                phone_number = self.get_new_customer_phone_number_via_input(customers)
                break

        return phone_number


    def add_new_customer_via_input(self, customers):
        phone_number = self.get_new_customer_phone_number_via_input(customers)
        forename = input('Please enter forename: ')
        surname = input('Please enter surname: ')
        email = input('Please enter email address: ')
        postcode = input('Please enter postcode: ')

        new_customer = Customer(forename, surname, phone_number, email, postcode)
        customers.add(new_customer)

        print()
        print('Customer is successfully added.')
        print()


    def main(self, customers):
        Utils.clear_screen()

        self.display_options()

        selection = self.get_selection_via_input()

        if selection == 1:
            Utils.clear_screen()
            print('Selected: 1. View existing Customers')
            self.view_customers(customers)
            input('Press Enter to go back to Menu...')
            self.main(customers)

        elif selection == 2:
            Utils.clear_screen()
            print('Selected: 2. Add Customer')
            self.add_new_customer_via_input(customers)
            input('Press Enter to go back to Menu...')
            self.main(customers)

        elif selection == 3:
            Utils.clear_screen()
            print('Exiting...')