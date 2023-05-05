from lib.menu import Menu
from unittest.mock import Mock
from lib.dish import Dish
"""
Given a menu and an instance of a dish,
I can add a dishes to it which should initially be available
"""
def test_add_dishes_to_menu():
    menu = Menu()
    dish_mock = Mock()
    menu.add_dish(dish_mock)
    assert menu.dishes[dish_mock] == True

"""
Given a menu with dishes
all available dish items should be printed with their name and price
"""
def test_display_menu():
    menu = Menu()
    pasta_dish_mock = Mock()
    rice_dish_mock = Mock()
    pasta_dish_mock.name = "Pasta"
    pasta_dish_mock.price = 10.0
    rice_dish_mock.name = "Rice"
    rice_dish_mock.price = 8.0
    menu.add_dish(pasta_dish_mock)
    menu.add_dish(rice_dish_mock)
    assert menu.display_menu() == "Pasta: 10.0€ Rice: 8.0€ "

"""
Given a specific dish which is part of a menu,
I want to make the dish unavailable and available again
"""
def test_make_dish_unavailable_and_available_again():
    menu = Menu()
    pasta_dish_mock = Mock()
    menu.add_dish(pasta_dish_mock)
    menu.set_dish_unavailable(pasta_dish_mock)
    print(menu.dishes[pasta_dish_mock])
    assert menu.dishes[pasta_dish_mock] == False
    menu.set_dish_available(pasta_dish_mock)
    assert menu.dishes[pasta_dish_mock] == True