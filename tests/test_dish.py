from lib.dish import Dish

"""
Given a dish name and price
Makes sure a dish item is created
"""
def test_dish_initialisation_with_name_and_price():
    puttanesca_dish = Dish("puttanesca", 14.5)
    assert puttanesca_dish.price == 14.5
    assert puttanesca_dish.name == "puttanesca"