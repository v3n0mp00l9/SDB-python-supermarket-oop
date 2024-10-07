from service import *
from entities import *

class UI:
    def __init__(self, service : Service):
        self.__service = service

    def __print_main_menu(self):
        print('1. Admin Menu')
        print('2. Client Menu')
        print('0. Back')

    def __print_admin_menu(self):
        print('1. Add a product in the product list')
        print('2. Delete a product from the product list by barcode')
        print('3. Modify a product from the product list by barcode')
        print('4. Show all products from the product list')
        print('5. Show all products from a specified company')
        print('6. Add a new promotion to the promotions list')
        print('7. Add a product to a specified promotion from the promotions list by barcode')
        print('8. Show all promotions')
        print('9. Show all products from a promotion')
        print('0. Back')

    def __print_client_menu(self):
        print('1. Show all products from the products list')
        print('2. Buy a certain amount of a specified product')
        print('3. Show all products that have a smaller price than the one specified')
        print('4. Show all promotions')
        print('5. Show all products in a promotion')
        print('0. Back')

    def __add_product(self):
        # adds the product with the desired atributes to the list 
        barcode = input('Barcode: ')
        name = input('Name: ')
        company = input('Company: ')
        price = int(input('Price: '))
        amount = int(input('Amount: '))
        self.__service.add_product(Product(barcode, name, company, price, amount))

    def __delete_product_by_barcode(self):
        barcode = input('Barcode: ')
        self.__service.delete_product_by_barcode(barcode)

    def __modify_product_by_barcode(self):
        barcode = input('Barcode: ')
        self.__service.modify_product_by_barcode(barcode)

    def __show_all_products(self):
        self.__service.show_list_of_products()

    def __show_all_products_from_company(self):
        company = input('Company: ')
        self.__service.show_all_products_from_specified_company(company)

    def __add_new_promotion(self):
        percentage = int(input('New percentage for the promotion'))
        self.__service.add_new_promotion(percentage)

    def __add_product_to_specified_promotion(self):
        barcode = input('Barcode: ')
        index = int(input('Index of the promotion: ')) - 1
        self.__service.add_item_to_specified_promotion_by_barcode(index, barcode)

    def __show_all_promotions(self):
        self.__service.show_all_promotions()

    def __show_all_products_from_promotion(self):
        index = int(input('Index of the promotion: ')) - 1
        self.__service.show_all_products_from_specified_promotion(index)

    def __buy_certain_amount(self):
        barcode = input('Barcode: ')
        amount = int(input('Amount: '))
        self.__service.buy_x_amount_of_product_by_barcode(barcode, amount)

    def __show_products_with_smaller_price(self):
        price = input('Maximum price that you can afford: ')
        self.__service.show_products_below_certain_price(price)

    def __run_admin_menu(self):
        while True:
            self.__print_admin_menu()
            try:
                command = int(input('Choose the command: '))
                if command == 0:
                    break
                elif command == 1:
                    self.__add_product()
                elif command == 2:
                    self.__delete_product_by_barcode()
                elif command == 3:
                    self.__modify_product_by_barcode()
                elif command == 4:
                    self.__show_all_products()
                elif command == 5:
                    self.__show_all_products_from_company()
                elif command == 6:
                    self.__add_new_promotion()
                elif command == 7:
                    self.__add_product_to_specified_promotion()
                elif command == 8:
                    self.__show_all_promotions()
                else:
                    self.__show_all_products_from_promotion()
            except ValueError as err:
                print(err)

    def __run_client_menu(self):
        while True:
            self.__print_client_menu()
            try:
                command = int(input('Choose the command: '))
                if command == 0:
                    break
                elif command == 1:
                    self.__show_all_products()
                elif command == 2:
                    self.__buy_certain_amount()
                elif command == 3:
                    self.__show_products_with_smaller_price()
                elif command == 4:
                    self.__show_all_promotions()
                elif command == 5:
                    self.__show_all_products_from_promotion()
            except ValueError as err:
                print(err)

    def run(self):
        while True:
            self.__print_main_menu()
            command = int(input('Choose the option: '))
            if command == 0:
                break
            elif command == 1:
                self.__run_admin_menu()
            else:
                self.__run_client_menu()


