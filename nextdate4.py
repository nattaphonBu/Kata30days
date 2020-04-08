import unittest
from datetime import date


def next_day(today):
    if today.month == 12:
        year = today.year + 1
        next_day = date(year,1,1)
    elif today.day == 31 or today.day == 30:
        month = today.month + 1
        next_day = date(2020,month,1)
    else:
        day = today.day + 1
        month = today.month
        next_day = date(2020,month,day)
    return next_day

class NextDayTest(unittest.TestCase):
    def test_1_1_2020_should_show_2_1_2020(self):
        today = date(2020,1,1)
        expected = date(2020,1,2)
        
        actual = next_day(today)
        self.assertEqual(actual, expected)
        
    def test_10_1_2020_should_show_11_1_2020(self):
        today = date(2020,1,10)
        expected = date(2020,1,11)
    
        actual = next_day(today)
        self.assertEqual(actual, expected)
        
    def test_10_2_2020_should_show_11_2_2020(self):
        today = date(2020,2,10)
        expected = date(2020,2,11)
        
        actual = next_day(today)
        self.assertEqual(actual, expected)
        
    def test_10_3_2020_should_show_11_3_2020(self):
        today = date(2020,3,10)
        expected = date(2020,3,11)
        
        actual = next_day(today)
        self.assertEqual(actual, expected)
        
    def test_31_3_2020_should_show_1_4_2020(self):
        today = date(2020,3,31)
        expected = date(2020,4,1)
        
        actual = next_day(today)
        self.assertEqual(actual, expected)
        
    def  test_30_4_2020_should_show_1_5_2020(self):
        today = date(2020,4,30)
        expected = date(2020,5,1)
        
        actual = next_day(today)
        self.assertEqual(actual, expected)
        
    def test_31_12_2020_should_show_1_1_2021(self):
        today = date(2020,12,31)
        expected = date(2021,1,1)
        
        actual = next_day(today)
        self.assertEqual(actual, expected)
        
    def test_31_12_2019_should_show_1_1_2020(self):
        today = date(2019,12,31)
        expected = date(2020,1,1)
        
        actual = next_day(today)
        self.assertEqual(actual, expected)
        
    def test_31_12_2021_should_show_1_1_2022(self):
        today = date(2021,12,31)
        expected = date(2022,1,1)
        
        actual = next_day(today)
        self.assertEqual(actual, expected)
        
                
unittest.main()
