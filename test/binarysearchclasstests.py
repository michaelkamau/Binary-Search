import unittest
from binary_search_src.binary_search import BinarySearch


class ListComprehensionTest(unittest.TestCase):
    """Binary Search to traverse an ordered list, effectively
       Populate the arrays with valid content
    """

    def setUp(self):
        self.one_to_twenty = BinarySearch(20, 1)
        self.two_to_forty = BinarySearch(20, 2)
        self.ten_to_thousand = BinarySearch(100, 10)

    def test_small_list(self):
        self.assertListEqual(
            [1, 20, 20],
            [
                self.one_to_twenty[0],
                self.one_to_twenty[19],
                self.one_to_twenty.length
            ],
            msg='should create an array from 1 to 20, with intervals of 1'
        )
        for index, number in enumerate(self.one_to_twenty):
            if index < self.one_to_twenty.length - 1:
                self.assertEqual(
                    1,
                    self.one_to_twenty[index + 1] - self.one_to_twenty[index],
                    msg='should return 1 for consequtive numbers'
                )

    def test_medium_list(self):
        self.assertListEqual(
            [2, 40, 20],
            [
                self.two_to_forty[0],
                self.two_to_forty[19],
                self.two_to_forty.length
            ],
            msg='should create an array from 2 to 40, with intervals of 2'
        )
        for index, number in enumerate(self.two_to_forty):
            if index < self.two_to_forty.length - 1:
                self.assertEqual(
                    2,
                    self.two_to_forty[index + 1] - self.two_to_forty[index],
                    msg='should return 2 for consequtive numbers')