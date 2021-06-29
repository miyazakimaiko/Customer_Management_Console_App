from Classes.customer import Customer
from Classes.customers import Customers
from Classes.mainmenu import MainMenu

customers = Customers()

customers.add(Customer('Maiko', 'Miyazaki', '0834837641', 'sample@test.com', 'D12 DVY5'))
customers.add(Customer('James', 'Brown', '0874837641', 'sample@test.com', 'D17 DRS2'))
customers.add(Customer('Tara', 'White', '0832937641', 'sample@test.com', 'D09 E5Y5'))

mainmenu = MainMenu()
mainmenu.main(customers)