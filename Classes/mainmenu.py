from .utils import Utils

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
        print('Name: '.ljust(30) + 'Phone Number: '.ljust(30) + 'Email Address: '.ljust(30) + 'Postcode: '.ljust(30))
        print(''.ljust(100, '-'))

        for customer in customers.group:
            print(customer)


    def main(self, customers):
        Utils.clear_screen()

        self.display_options()

        selection = self.get_selection_via_input()

        if selection == 1:
            Utils.clear_screen()
            print('Selected: 1. View existing Customers')
            self.view_customers(customers)

        elif selection == 2:
            Utils.clear_screen()
            print('Selected: 2. Add Customer')

        elif selection == 3:
            Utils.clear_screen()
            print('Exiting...')