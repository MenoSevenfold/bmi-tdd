import unittest
from Sortbubble import bubblesort
from Sortbubble import check

class MyTestCase(unittest.TestCase):

    def test_list(self):
        # stub
        stub1 = [3,6,9,1]
        stub2 = [0,7,2,3,4]
        stub3 = []

        # assume
        expected1 = [1,3,6,9]
        expected2 = [0,2,3,4,7]
        expected3 = "no input"

        # action
        result1 = bubblesort(stub1)
        result2 = bubblesort(stub2)
        result3 = bubblesort(stub3)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)


    def cheack_list(self):
        # stub
        stub1 = [2,5,8,1]
        stub2 = [0,8,3,4,5]


        # assume
        expected1 = True
        expected2 = False

        # action
        result_check1 = check(stub1)
        result_check2 = check(stub2)


        # expect/assert
        self.assertEqual(result_check1, expected1)
        self.assertEqual(result_check2, expected2)



if __name__ == '__main__':
    unittest.main()
