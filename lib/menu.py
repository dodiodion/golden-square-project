class Menu:
    # class properties: 
        #   dishes: dictionary representing all available dishes of the menu, and if they are available or not
        #        ex. {dish_fish: True, dish_paella: False, pasta_tomatoes: True}

    def __init__(self):
        self.dishes = {}

    def add_dish(self, dish):
        # Parameter:
        #   dish: the dish to be added to the menu
        # Side Effects: 
        #   adds a dish to the list of dishes of the menu
        self.dishes[dish] = True

    def display_menu(self):
        # Returns:
        #   A formatted string representing the menu with dish names and prices
        display_string = ""
        for dish_item, is_available in self.dishes.items():
            if is_available == True:
                display_string += f"{dish_item.name}: {dish_item.price}€ "
        return display_string


    def set_dish_unavailable(self, dish):
        # Parameters:
        #   dish: the dish that needs to be set unavailable
        # Side Effects:
        #   sets a given dish as unavailable, if it is in the dish list
        if dish in self.dishes.keys():
            self.dishes[dish] = False

    def set_dish_available(self, dish):
        # Parameters:
        #   dish: the dish that needs to be set as available
        # Side Effects:
        #   sets a given dish as available, if it is in the dish list
        if dish in self.dishes.keys():
            self.dishes[dish] = True