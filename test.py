import util
import colorama
from termcolor import colored, cprint
from pynput import keyboard
import unittest


class test_methods(unittest.TestCase):

    def test_is_valid_sepetation(self):
        self.assertTrue(util.is_valid_seperation(2, 2, 8, 8))

    def test_get_neighboord(self):
        self.assertIsNotNone(util.get_neighboord(1, 1, 8, 8))

        colorama.init()

        test = [
            [" ", "1:s", "2", "3", "4", "5", "6", "7", "8"],
            ["1", " ", "F", "F", "2", " ", " ", " ", " "],
            ["2", "F", "F", "1", "M", " ", " ", " ", " "],
            ["3", " ", " ", " ", " ", " ", " ", " ", " "],
            ["4", " ", "F", "F", "2", "M", " ", " ", " "],
            ["5", " ", "F", "F", "2", " ", " ", " ", " "],
            ["6", " ", "F", "F", "2", " ", " ", " ", " "],
            ["7", " ", "F", "F", "2", " ", " ", " ", " "],
            ["8", " ", "F", "F", "2", " ", " ", " ", " "],
        ]

        # util.print_table(test)


if __name__ == '__main__':
    unittest.main()
