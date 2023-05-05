class Order:
    # class properties: 
        #   ordered_dishes: dictionary of all dishes selected by the customer with the number of occurance
        #   ex. {dish_fish: 5, dish_paella: 2, pasta_tomatoes: 1}
        #   is_completed: true if the order has been confirmed and paid
        #   menu: menu from which the order is being taken
    def __init__(self, menu):
        self.is_completed = False
        self.ordered_dishes = {}
        self.menu = menu

    def print_receipt(self):
        # prints a summary of the order, with the list of items and how many times they were orders and the grand total
        receipt_string = ""
        for dish, number in self.ordered_dishes.items():
            price = number * dish.price
            receipt_string += f"{number} {dish.name}: {price}€ "
        receipt_string += f"Total: {self.get_total_price()}€"
        return receipt_string

    def get_total_price(self):
        # Returns :
        #   the total price of the order (sum of the prices of all item ordered)
        total = 0.0
        for dish, number in self.ordered_dishes.items():
            total += dish.price * number
        return total

    def select_dish(self, dish):
        # Parameters:
        #   dish:  the dish to be added to the ordered dishes
        # Side Effects:
        #   adds the selected dish to the dictionary of ordered items
        #if dish not in self.menu.keys() or self.menu[dish] == False:
        #    raise Exception("Cannot chose this item since it is not part of the menu")
        if dish in self.ordered_dishes.keys():
            self.ordered_dishes[dish] += 1
        else:
            self.ordered_dishes[dish] = 1

    def complete_order(self, dish):
        # Side Effects:
        #   sends receipt via SMS
        pass
