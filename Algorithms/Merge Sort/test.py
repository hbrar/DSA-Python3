import Implementation
import unittest

# class name can be arbitrary
class FibTest(unittest.TestCase):
    # FibTest is inheriting from class unittest.TestCase
    
    arr1 = [3, 6, 4, 1, 9, 5]
    sortedArr1 = Implementation.mSort(arr1)
    expctArr1 = [1, 3, 4, 5, 6, 9]
    
    # duplicates
    arr2 = [3, 6, 4, 1, 4, 9, 3]
    sortedArr2 = Implementation.mSort(arr2)
    expctArr2 = [1, 3, 3, 4, 4, 6, 9]
    
    arr3 = [0, 1, 0, 1, 0, 1, 0]
    sortedArr3 = Implementation.mSort(arr3)
    expctArr3 = [0, 0, 0, 0, 1, 1, 1]
    
    arr4 = [1,0]
    sortedArr4 = Implementation.mSort(arr4)
    expctArr4 = [0,1]
    
    # one element
    arr5 = [0]
    sortedArr5 = Implementation.mSort(arr5)
    expctArr5 = [0]
    
    # empty array
    arr6 = []
    sortedArr6 = Implementation.mSort(arr6)
    expctArr6 = []
    
    # reverse array
    arr7 = [4,3,2,1]
    sortedArr7 = Implementation.mSort(arr7)
    expctArr7 = [1,2,3,4]
    
    # The test cases are defined in this class by using methods
    # name of these methods is arbitrary, but has to start with test
    def testCases(self):
        self.assertEqual(isArrEq(self.sortedArr1,self.expctArr1), True)
        self.assertEqual(isArrEq(self.sortedArr2,self.expctArr2), True)
        self.assertEqual(isArrEq(self.sortedArr3,self.expctArr3), True)
        self.assertEqual(isArrEq(self.sortedArr4,self.expctArr4), True)
        self.assertEqual(isArrEq(self.sortedArr5,self.expctArr5), True)
        self.assertEqual(isArrEq(self.sortedArr6,self.expctArr6), True)
        self.assertEqual(isArrEq(self.sortedArr7,self.expctArr7), True)
        
def isArrEq(sortedArr,expctArr):
    for i in range(len(expctArr)):
        if sortedArr[i] != expctArr[i]:
            return False
    return True

if __name__ == "__main__":
    unittest.main()
