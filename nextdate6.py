import unittest
from datetime import date


def next_day(today):
    if today.day == 31 or today.day == 30:
        nextday = date(2020, today.month + 1, 1)
    else:
        day = today.day + 1
        month = today.month
        nextday = date(2020, month, day)
    return nextday


class NextDateTest(unittest.TestCase):
    def test_2_1_2020_should_show_3_1_2020(self):
        today = date(2020, 1, 2)
        expected = date(2020, 1, 3)

        actual = next_day(today)
        self.assertEqual(actual, expected)

    def test_15_1_2020_should_show_16_1_2020(self):
        today = date(2020, 1, 15)
        expected = date(2020, 1, 16)

        actual = next_day(today)
        self.assertEqual(actual, expected)

    def test_2_2_2020_should_show_3_2_2020(self):
        today = date(2020, 2, 2)
        expected = date(2020, 2, 3)

        actual = next_day(today)
        self.assertEqual(actual, expected)

    def test_31_3_2020_should_show_1_4_2020(self):
        today = date(2020, 3, 31)
        expected = date(2020, 4, 1)

        actual = next_day(today)
        self.assertEqual(actual, expected)
        
    def test_30_4_2020_should_show_1_5_2020(self):
        today = date(2020,4,30)
        expected = date(2020,5,1)
        
        actual = next_day(today)
        self.assertEqual(actual, expected)

unittest.main()
