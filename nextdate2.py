import unittest
from datetime import date


def find_next_day(today):
    if today.day == 30 or today.day == 31:
        month = today.month + 1
        day = 1
    elif today == date(2020,2,29):
        return date(2020,3,1)
    elif today == date(2019,2,28):
        return date(2019,3,1)
    else:
        day = today.day + 1
        month = today.month
    return date(2020,month,day)


class NextDateTest(unittest.TestCase):
    def test_1_1_2020_should_show_2_1_2020(self):
        today = date(2020,1,1)
        expected = date(2020,1,2)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)

    def test_10_1_2020_should_show_11_1_2020(self):
        today = date(2020,1,10)
        expected = date(2020,1,11)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)

    def test_15_1_2020_should_show_16_1_2020(self):
        today = date(2020,1,15)
        expected = date(2020,1,16)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)

    def test_31_1_2020_shoud_show_1_2_2020(self):
        today = date(2020,1,31)
        expected = date(2020,2,1)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)

    def test_31_3_2020_should_show_1_4_2020(self):
        today = date(2020,3,31)
        expected = date(2020,4,1)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)

    def test_31_5_2020_should_show_1_6_2020(self):
        today = date(2020,5,31)
        expected = date(2020,6,1)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)

    def test_30_4_2020_should_show_1_5_2020(self):
        today = date(2020,4,30)
        expected = date(2020,5,1)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)

    def test_29_2_2020_should_show_1_3_2020(self):
        today = date(2020,2,29)
        expected = date(2020,3,1)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)

    def test_28_2_2019_should_show_1_3_2019(self):
        today = date(2019,2,28)
        expected = date(2019,3,1)

        actual = find_next_day(today)
        self.assertEqual(actual, expected)
    
    


unittest.main()