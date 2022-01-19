import unittest
import solution

class TestStringMethods(unittest.TestCase):

    def test_base_case(self):
        self.assertEqual(solution.count_clicks('{"amazon.com":23,"google.co.uk":15,"google.com":7,"amazon.co.uk":9,"london.gov.uk":4}'), {'amazon.com': 23, 'com': 30, 'google.co.uk': 15, 'uk': 28, 'co.uk': 24, 'google.com': 7, 'amazon.co.uk': 9, 'london.gov.uk': 4, 'gov.uk': 4}
                         )

    def test_case1(self):
        self.assertEqual(solution.count_clicks('{"google.co.uk":15}'), {
                         'google.co.uk': 15, 'uk': 15, 'co.uk': 15})

    def test_case2(self):
        self.assertEqual(solution.count_clicks('{"amazon.com":23,"google.co.uk":15}'), {
                         'amazon.com': 23, 'com': 23, 'google.co.uk': 15, 'uk': 15, 'co.uk': 15})

    
if __name__ == '__main__':
    unittest.main()