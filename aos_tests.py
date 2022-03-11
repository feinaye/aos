import unittest
import aos_locators as locators
import aos_methods as methods

class AOSAppPositiveTestCases(unittest.TestCase):

    @staticmethod
    def test_create_new_user():

        methods.set_up()
        methods.create_new_account()
        methods.sign_out()
        methods.log_in()
        methods.sign_out()
        methods.tear_down()
