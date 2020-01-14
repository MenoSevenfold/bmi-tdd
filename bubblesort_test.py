import unittest
from Sortbubble import bubblesort

class MyTestCase(unittest.TestCase):
    def short_list(lst):
        for i in lst:
            if lst[i]>lst[i+1]:
                return False
        else: return True
    def test_list(self):
        # stub
        stub1 = [3,6,9,1]
        stub2 = [0,7,2,3,4]
        stub3 = []

        # assume
        expected1 = [1,3,6,9]
        expected2 = [0,2,3,4,7]
        expected3 = "no imput"

        # action
        result1 = bubblesort(stub1)
        result2 = bubblesort(stub2)
        result3 = bubblesort(stub3)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)

        #self.assertEqual(True, False)
    def short_list(self):
        # stub
        stub1 = [2,5,8,1]
        stub2 = [0,8,3,4,5]
        stub3 = []

        # assume
        expected1 = True
        expected2 = True
        expected3 = True

        # action
        result1 = short_list(bubbleSort(stub1))
        result2 = short_list(bubbleSort(stub2))
        result3 = bubblesort(stub3)

        # expect/assert
        self.assertEqual(result1, expected1)
        self.assertEqual(result2, expected2)
        self.assertEqual(result3, expected3)


if __name__ == '__main__':
    unittest.main()
