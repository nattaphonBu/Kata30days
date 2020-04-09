import unittest
from datetime import date


def next_day(today):
    if today.month == 12:
        nextday = date(today.year + 1,1,1)
    elif today.day == 31 or today.day == 30 :
        nextday = date(2020,today.month + 1,1)
    elif today == date(2020,2,29):
        nextday = date(2020,3,1)
    else:
        day = today.day + 1
        month = today.month
        nextday = date(2020, month, day)
    return nextday


class NextDayTest(unittest.TestCase):
    def test_1_1_2020_should_show_2_1_2020(self):
        today = date(2020, 1, 1)
        expected = date(2020, 1, 2)

        actual = next_day(today)
        self.assertEqual(actual, expected)

    def test_15_1_2020_should_show_16_1_2020(self):
        today = date(2020, 1, 15)
        expected = date(2020, 1, 16)

        actual = next_day(today)
        self.assertEqual(actual, expected)

    def test_1_2_2020_should_show_2_2_2020(self):
        today = date(2020, 2, 1)
        expected = date(2020, 2, 2)

        actual = next_day(today)
        self.assertEqual(actual, expected)

    def test_14_2_2020_should_show_15_2_2020(self):
        today = date(2020,2,14)
        expected = date(2020,2,15)
        
        actual = next_day(today)
        self.assertEqual(actual, expected)
        
    def test_31_3_2020_should_show_1_4_2020(self):
        today = date(2020,3,31)
        expected = date(2020,4,1)
        
        actual = next_day(today)
        self.assertEqual(actual, expected)
        
    def test_30_4_2020_should_show_1_5_2020(self):
        today = date(2020,4,30)
        expected = date(2020,5,1)
        
        actual = next_day(today)
        self.assertEqual(actual, expected)
        
    def test_31_12_2019_should_show_1_1_2020(self):
        today = date(2019,12,31)
        expected = date(2020,1,1)
        
        actual = next_day(today)
        self.assertEqual(actual, expected)
    
    def test_31_12_2020_should_show_1_1_2021(self):
        today = date(2020,12,31)
        expected = date(2021,1,1)
        
        actual = next_day(today)
        self.assertEqual(actual, expected)
        
    def test_29_2_2020_should_show_1_3_2020(self):
        today = date(2020,2,29)
        expected = date(2020,3,1)
        
        actual = next_day(today)
        self.assertEqual(actual, expected)
        
unittest.main()
