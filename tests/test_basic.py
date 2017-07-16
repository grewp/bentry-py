# -*- coding: utf-8 -*-

# from .context import core
# from context import bentry

import unittest


# TODO
# 1. get function import working
# 2. mock out an example budget sheet
# 3. seperate program functionality into unit testable components


def add(x, y):
    return x + y


class findOpenCell(unittest.TestCase):
    """findOpenCell() tests"""

    def test_absolute_truth_and_meaning(self):
        self.assertEqual(add(2,2), 4)

    def test_absolute_truth(self):
        self.assertEqual(add(2,4), 4)

    # TODO move this to unit tests
    # # findOpenCellUnit tests
    # print findOpenCell((7,1)) # expect (12,1)
    # print findOpenCell((2,3)) # expect (2,3)
    # print findOpenCell((7,4)) # expect (9,4)


if __name__ == '__main__':
    unittest.main()
