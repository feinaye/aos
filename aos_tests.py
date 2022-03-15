import unittest
import aos_locators as locators
import aos_methods as methods

class AOSAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_create_new_user():

        methods.set_up()
        methods.validate_homepage()
        methods.create_new_account()
        methods.sign_out()
        methods.log_in()
        methods.checkout_shopping_cart()
        methods.tear_down()
