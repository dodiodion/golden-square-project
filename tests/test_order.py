from lib.order import Order
from unittest.mock import Mock
import pytest

"""
given a menu, 
An order should be initialised as being uncompleted with an empty list of dishes
"""
def test_create_new_order_is_uncompleted():
    menu = Mock()
    order = Order(menu)
    assert order.is_completed == False
    assert order.ordered_dishes == {}

"""
Given an dish item on the menu,
If the item is selected two times, i should have 2 as the value of the
    ordered_dishes dictionary with the given dish as a key
"""
def test_select_dish_to_order():
    menu_mock = Mock()
    order = Order(menu_mock)
    couscous_dish = Mock()
    #menu_mock[couscous_dish] = True
    order.select_dish(couscous_dish)
    order.select_dish(couscous_dish)
    assert order.ordered_dishes[couscous_dish] == 2

"""
Given an dish item that is not on the menu or that is unavailable,
the item shouldnt be added and an error message should be sent.
"""
# def test_select_dish_to_order():
#     menu_mock = Mock()
#     order = Order(menu_mock)
#     couscous_dish = Mock()
#     #menu_mock.dishes[couscous_dish] = False
#     #with pytest.raises(Exception) as e: 
#     #    order.select_dish(couscous_dish)
#     #error_message = str(e.value)
#     #assert error_message == "No reminder set!"
#     order.select_dish(couscous_dish)
#     assert order.ordered_dishes[couscous_dish] == 2

"""
Given an order with a few dishes
The total price is returned correctly
"""
def test_get_total():
    menu = Mock()
    order = Order(menu)
    pizza_dish_mock = Mock()
    pasta_dish_mock = Mock()
    pizza_dish_mock.price = 15.0
    pasta_dish_mock.price = 16.2
    order.select_dish(pizza_dish_mock)
    order.select_dish(pasta_dish_mock)
    assert order.get_total_price() == 31.2

"""
Given an order,
The receipt is given as a formatted list of all dishes ordered, and includes the total price
"""
def test_print_receipt():
    menu = Mock()
    order = Order(menu)
    pizza_dish_mock = Mock()
    pasta_dish_mock = Mock()
    pizza_dish_mock.name = "Pizza"
    pasta_dish_mock.name = "Pasta"
    pizza_dish_mock.price = 15.0
    pasta_dish_mock.price = 16.2
    order.select_dish(pizza_dish_mock)
    order.select_dish(pizza_dish_mock)
    order.select_dish(pasta_dish_mock)
    assert order.print_receipt() == "2 Pizza: 30.0€ 1 Pasta: 16.2€ Total: 46.2€"