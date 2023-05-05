from lib.dish import Dish
from lib.menu import Menu
from lib.order import Order

"""
given a menu, 
An order should be initialised as being uncompleted with an empty list of dishes
"""
def test_create_new_order_is_uncompleted():
    menu = Menu()
    order = Order(menu)
    assert order.is_completed == False
    assert order.ordered_dishes == {}

"""
Given an order,
The receipt is given as a formatted list of all dishes ordered, and includes the total price
"""
def test_print_receipt():
    sushi_dish = Dish("Sushi", 20.0)
    pizza_dish = Dish("Pizza", 14.5)
    tacos_dish = Dish("Tacos", 13.2)
    menu = Menu()
    menu.add_dish(sushi_dish)
    menu.add_dish(pizza_dish)
    menu.add_dish(tacos_dish)
    order = Order(menu)
    order.select_dish(sushi_dish)
    order.select_dish(sushi_dish)
    order.select_dish(tacos_dish)
    assert order.print_receipt() == "2 Sushi: 40.0€ 1 Tacos: 13.2€ Total: 53.2€"


"""
Given an order with a few dishes
The total price is returned correctly
"""
def test_get_total():
    menu = Menu()
    order = Order(menu)
    pizza_dish = Dish("Pizza", 15.0)
    pasta_dish = Dish("Pasta", 16.2)
    order.select_dish(pizza_dish)
    order.select_dish(pasta_dish)
    order.select_dish(pizza_dish)
    assert order.get_total_price() == 46.2

    """
Given an dish item on the menu,
If the item is selected two times, i should have 2 as the value of the
    ordered_dishes dictionary with the given dish as a key
"""
def test_select_dish_to_order():
    menu = Menu()
    order = Order(menu)
    couscous_dish = Dish("Couscous", 34.5)
    order.select_dish(couscous_dish)
    order.select_dish(couscous_dish)
    assert order.ordered_dishes[couscous_dish] == 2