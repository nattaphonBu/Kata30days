import unittest
from  datetime import date

def find_next_day(today):
    day = today.day + 1
    month = today.month
    return date(2020, month, day)

         

class NextDateTest(unittest.TestCase):
    def test_1_1_2020_should_show_2_1_2020(self):
        today = date(2020, 1, 1)
        expected = date(2020, 1, 2)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)

    def test_5_1_2020_should_show_6_1_2020(self):
        today = date(2020, 1, 5)
        expected = date(2020, 1, 6)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)
    
    def test_10_1_2020_should_show_11_1_2020(self):
        today = date(2020, 1, 10)
        expected = date(2020, 1, 11)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)

    def test_15_1_2020_should_show_16_1_2020(self):
        today = date(2020, 1, 15)
        expected = date(2020, 1, 16)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)
    
    def test_1_2_2020_should_show_2_2_2020(self):
        today = date(2020, 2, 1)
        expected = date(2020, 2, 2)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)

    def test_15_2_2020_should_show_16_2_2020(self):
        today = date(2020, 2, 15)
        expected = date(2020, 2, 16)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)
    
    def test_10_3_2020_should_show_11_3_2020(self):
        today = date(2020, 3, 10)
        expected = date(2020, 3, 11)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)


unittest.main()