class Product:
    def __init__(self, barcode, name, company, price, amount):
        self.__barcode = barcode
        self.__name = name
        self.__company = company
        self.__price = price
        self.__amount = amount

    def get_barcode(self):
        return self.__barcode

    def get_name(self):
        return self.__name

    def get_company(self):
        return self.__company

    def get_price(self):
        return self.__price

    def get_amount(self):
        return self.__amount

    def set_barcode(self, new_barcode):
        self.__barcode = new_barcode

    def set_name(self, new_name):
        self.__name = new_name

    def set_company(self, new_company):
        self.__company = new_company

    def set_price(self, new_price):
        self.__price = new_price

    def set_amount(self, new_amount):
        self.__amount = new_amount

    def __str__(self):
        return f'Barcode : {self.__barcode}, Name : {self.__name}, Company : {self.__company}, Price : {self.__price}, Amount : {self.__amount}'


class Promotion:
    def __init__(self, percentage, list_of_items):
        self.__percentage = percentage
        self.__list_of_items = list_of_items

    def get_percentage(self):
        return self.__percentage

    def get_list_of_items(self):
        return self.__list_of_items

    def print_list_of_items(self):
        for product in self.__list_of_items:
            print(product)

    def set_percentage(self, new_percentage):
        self.__percentage = new_percentage

    def add_item_to_list(self, item_to_be_added):
        self.__list_of_items.append(item_to_be_added)

    def remove_item_from_list(self, item_to_be_removed):
        for item in self.__list_of_items:
            if item == item_to_be_removed:
                del item

    def __str__(self):
        return f'Percentage: {self.__percentage}, List: {self.__list_of_items}'
