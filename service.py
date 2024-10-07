from entities import *

class Service:
    def __init__(self):
        self.__product_list = [Product('placeholder', 'placeholder', 'placeholder', 0, 0)]
        self.__promotion_list = [Promotion(0, [Product('placeholder', 'placeholder', 'placeholder', 0, 0)])]

    def add_product(self, new_product):
        # adds a product to the list if it doesn't already exist in it
        for product in self.__product_list:
            if product == new_product:
                raise ValueError(f'The product {new_product} is already on the list')
        self.__product_list.append(new_product)

    def show_list_of_products(self):
        # shows all the products in the list in the order they were entered , if any
        if len(self.__product_list) == 0:
            raise ValueError('No products in the list')
        for product in self.__product_list:
            print(product)

    def show_all_products_from_specified_company(self, company):
        # shows all product from a specified company by name
        for product in self.__product_list:
            if product.get_company() == company:
                print(product)

    def __find_index_of_product_by_barcode(self, barcode):
        # private function
        # find the position of the product with the desired barcode ,
        # returns None if not found in the list to eliminate edge cases
        for i in range(len(self.__product_list)):
            if self.__product_list[i].get_barcode() == barcode:
                return i
        return None

    def delete_product_by_barcode(self, barcode):
        # retrieves the desired position using the __find_index function
        # eliminates the product from the list , if found
        pos_to_delete = self.__find_index_of_product_by_barcode(barcode)
        if pos_to_delete is None:
            raise ValueError(f'The specified barcode {barcode} is not found in the list')
        del self.__product_list[pos_to_delete]

    def modify_product_by_barcode(self, barcode):
        # modifies the values of the product , one at the time
        # finds the position of the element to modify using the private function __find_index
        pos_to_modify = self.__find_index_of_product_by_barcode(barcode)
        if pos_to_modify is None:
            raise ValueError(f'The specified barcode {barcode} is not found in the list')
        print('What do you want to modify?')
        print('1. Barcode')
        print('2. Name')
        print('3. Company')
        print('4. Price')
        print('5. Amount')
        option = int(input())
        # using the setters in order to achieve the desired result
        if option == 1:
            new_barcode = input('Enter the new barcode: ')
            self.__product_list[pos_to_modify].set_barcode(new_barcode)
        elif option == 2:
            new_name = input('Enter the new name: ')
            self.__product_list[pos_to_modify].set_name(new_name)
        elif option == 3:
            new_company = input('Enter the new company: ')
            self.__product_list[pos_to_modify].set_company(new_company)
        elif option == 4:
            new_price = int(input('Enter the new price: '))
            self.__product_list[pos_to_modify].set_price(new_price)
        else:
            new_amount = int(input('Enter the new amount: '))
            self.__product_list[pos_to_modify].set_amount(new_amount)

    def add_new_promotion(self, new_percentage):
        # adds a new promotion to the promotions list
        # the list items in the new promotion is empty
        self.__promotion_list.append(Promotion(new_percentage, []))

    def show_all_promotions(self):
        # shows the promotions that have been entered by the admin of the shop
        # checks if the list is empty
        if len(self.__promotion_list) == 0:
            raise ValueError('No promotions in the list')
        for promotion in self.__promotion_list:
            print('Percentage: ', end='')
            print(promotion.get_percentage())
            promotion.print_list_of_items()

    def show_all_products_from_specified_promotion(self, index_of_promotion):
        # print(self.__promotion_list[index_of_promotion].get_list_of_items())
        self.__promotion_list[index_of_promotion].print_list_of_items()

    def add_item_to_specified_promotion_by_barcode(self, index_of_promotion, barcode):
        # Adds a product to a promotion from the list of promotions
        # The item is found by barcode
        pos = self.__find_index_of_product_by_barcode(barcode)
        if pos is None:
            raise ValueError(f'The specified barcode {barcode} is not found in the list')
        self.__promotion_list[index_of_promotion].add_item_to_list(self.__product_list[pos])

    def buy_x_amount_of_product_by_barcode(self, barcode, amount):
        # the customer can buy an x amount of items that are available in the inventory
        # raise error if the barcode does not exist
        # the customer is always right
        pos = self.__find_index_of_product_by_barcode(barcode)
        if pos is None:
            raise ValueError(f'The specified barcode {barcode} is not found in the list')
        if self.__product_list[pos].get_amount() < amount:
            raise ValueError('The specified amount is too big')
        current_amount = self.__product_list[pos].get_amount() - amount
        self.__product_list[pos].set_amount(current_amount)

    def __sort_by_price(self, product):
        # private function used in order to sort the products by price
        return product.get_price()

    def show_products_below_certain_price(self, price):
        # creates empty list , puts the products below the target price in it
        # sorts the list using the .sort() function with the default parameters changed
        # in order to reverse the prices order
        sorted_list = []
        for product in self.__product_list:
            if product.get_price() <= int(price):
                sorted_list.append(product)
        sorted_list.sort(reverse = True, key = self.__sort_by_price)
        for product in sorted_list:
            print(product)



