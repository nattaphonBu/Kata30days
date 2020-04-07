import unittest
from datetime import date


def next_date(today): 
    if today.day == 31:
        month = today.month + 1
        next_day = date(2020, month, 1)
    else:
        day = today.day + 1
        month = today.month  
        next_day = date(2020,month,day)
    return next_day

class NextDayTest(unittest.TestCase):
    def test_1_1_2020_shold_show_2_1_2020(self):
        today = date(2020,1,1)
        expected = date(2020,1,2)
        
        actual = next_date(today)
        self.assertEqual(actual, expected)
        
    def test_15_1_2020_should_show_16_1_2020(self):
        today = date(2020,1,15)
        expected = date(2020,1,16)
        
        actual = next_date(today)
        self.assertEqual(actual, expected)
        
    def test_20_1_2020_should_show_21_1_2020(self):
            today = date(2020,1,20)
            expected = date(2020,1,21)
            
            actual = next_date(today)
            self.assertEqual(actual, expected)
            
    def test_5_2_2020_should_show_6_2_2020(self):
        today = date(2020,2,5)
        expected = date(2020,2,6)
        
        actual = next_date(today)
        self.assertEqual(actual, expected)      
        
    
    def test_3_3_2020_should_show_4_3_2020(self):
        today = date(2020,3,3)
        expected = date(2020,3,4)
        
        actual = next_date(today)
        self.assertEqual(actual, expected)
        
    def test_30_3_2020_should_show_31_3_2020(self):
        today = date(2020,3,30)
        expected = date(2020,3,31)
        
        actual = next_date(today)
        self.assertEqual(actual, expected)
    
    def test_31_1_2020_should_show_1_2_2020(self):
        today = date(2020,1,31)
        expected = date(2020,2,1)
        
        actual = next_date(today)
        self.assertEqual(actual, expected)
        
    def test_31_3_2020_should_show_1_4_2020(self):
        today = date(2020, 3, 31)
        expected = date(2020,4,1)
        
        actual = next_date(today)
        self.assertEqual(actual, expected)

unittest.main()