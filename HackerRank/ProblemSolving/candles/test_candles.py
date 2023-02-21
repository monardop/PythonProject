import candles
import unittest

class CandlesTestCase(unittest.TestCase):
    
    def testbirthdayCakeCandles(self):
        array = [4, 3, 3, 4, 2]
        self.assertEqual(candles.birthdayCakeCandles(array), 2)
    
    def test2_birthdayCakeCandles(self):
        array = [1, 3, 3, 2, 2]
        self.assertEqual(candles.birthdayCakeCandles(array), 2)
