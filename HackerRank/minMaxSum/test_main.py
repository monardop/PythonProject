import unittest
import main


class miniMaxSumTestCase(unittest.TestCase):
    def testminiMaxSum(self):
        self.assertEqual(main.miniMaxSum([1, 2, 3, 4, 5]), "10 14")

        array = [769082435, 210437958, 673982045, 375809214, 380564127]
        self.assertEqual(main.miniMaxSum(array), "1640793344 2199437821")
