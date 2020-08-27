# Eliza Nip
# Summer 2020 CS325
# 07/07/2020
# HW2 Q2 Quick select

# Quick select 
# Ref from http://www.cs.yale.edu/homes/aspnes/pinewiki/QuickSelect.html?highlight=%28CategoryAlgorithmNotes%29
# Ref from https://stackoverflow.com/questions/36176907/implementation-of-the-quick-select-algorithm-to-find-kth-smallest-number
import random

# Set array.
# k -> kth smallest element of the array
def quick_select(k,array):
    if array == [] :
        return []
    # Let index be chosen in random, in range of array length
    index = random.randint(0,len(array)-1)
    # Pivot- A position that partitions the list into 2 parts. Left element < pivot and right element > pivot
    # Let pivot = array[index]
    pivot = array[index]
    # Set side
    array[0],pivot = pivot,array[0]
    # set Left element in array < pivot
    left = [i for i in array if i < pivot]
    # set Right element in array >= pivot
    right = [i for i in array[1:] if i >= pivot]

    # 3 if case: k = pivot; k> pivot; k< pivot
    if len(left) == k-1:
        return pivot
    elif len(left) < k-1:
        return quick_select(k-len(left)-1,right)
    else:
        return quick_select(k,left)
        
def main():
    print (quick_select(2,[1,2,3,4,5,6]))
    print (quick_select(3,[2,6,7,1,3,5]))

if __name__ == '__main__':
    main()
