from bubblesort import bubble 
from insertionSort import insertionSort
from selectionSort import selectionSort 

a = [3,1,2,4,94,1]
a2 = [-12,9874,9801234, -123,22,4,-14,9887,1234,0,-1423]
a3 = [1, 8, 2, 3, -4, 0, 10, 6]
print selectionSort(a3) == sorted(a3)
print selectionSort(a2) == sorted (a2)
print selectionSort(a) == sorted(a)