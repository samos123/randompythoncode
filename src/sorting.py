import copy
import unittest
import random

def insertion_sort_swap(list_to_sort):
    list_length = len(list_to_sort)
    for i in range(1, list_length):
        key = list_to_sort[i]
        j = i
        while j > 0 and list_to_sort[j-1] > key:
            list_to_sort[j], list_to_sort[j-1] = list_to_sort[j-1], list_to_sort[j]
            j -= 1

def insertion_sort_hole(list_to_sort):
    list_length = len(list_to_sort)
    for i in range(1, list_length):
        key = list_to_sort[i]
        j = i
        while j > 0 and list_to_sort[j-1] > key:
            list_to_sort[j] = list_to_sort[j-1]
            j -= 1
        list_to_sort[j] = key


def quick_sort(list_to_sort):
    if list_to_sort == []:
        return []
    else:
        pivot = list_to_sort[0]
        less = [i for i in list_to_sort[1:] if i < pivot]
        greater = [i for i in list_to_sort[1:] if i >= pivot]
        return quick_sort(less) + [pivot] + quick_sort(greater)
    
        

class SortingTestCase(unittest.TestCase):
    def setUp(self):
        self.test1 = [1,5,3,4]
        self.test2 = [2,4,5,5,6,1,3]
        self.test1_sorted = [1,3,4,5]
        self.test2_sorted = [1,2,3,4,5,5,6]

class InsertionSortTestCase(SortingTestCase):
    def test_1_swap(self):
        insertion_sort_swap(self.test1)
        self.assertEqual(self.test1, self.test1_sorted)
        
        insertion_sort_swap(self.test2)
        self.assertEqual(self.test2, self.test2_sorted)
        
    def test_2_holes(self):
        insertion_sort_hole(self.test2)
        self.assertEqual(self.test2, self.test2_sorted)
        
        insertion_sort_hole(self.test1)
        self.assertEqual(self.test1, self.test1_sorted)


class QuickSortTestCase(SortingTestCase):
    def test_1(self):
        sorted_list = quick_sort(self.test2)
        print sorted_list
        self.assertEqual(sorted_list, self.test2_sorted)


# Taken from somewhere but forgot where, fun to inspect at a later time
q=lambda x:(lambda o=lambda s:[i for i in x if cmp(i,x[0])==s]:len(x)>1 and q(o(-1))+o(0)+q(o(1)) or x)()

if __name__ == '__main__':
    unittest.main()
        
