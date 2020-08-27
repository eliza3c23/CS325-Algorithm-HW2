# Eliza Nip
# Summer 2020 CS325
# 07/07/2020
# HW2 Q3 Binary search

# Ref the python binsect library
# Ref the w3resource.com python search and sorting exercise
def binarysearch(k,array):
    # high default length of array
    # low default 0
    low, high = 0,len(array)
   
    while low < high:
        mid = (low + high) //2
        
        if array[mid] < k:
            low = mid + 1
        else:
            high = mid
    return low

# 2d array -> 1d array
# Use numpy to flatten 2D -> 1D. Numpy python library
# 1dArr = numpy.array([1,2,3],[4,5,6])
# 1dArr.flattern()
# Ref StackOverFlow metatArray method
# Create meta array -> bisect meta array to find array to look for the val, then bisect the found array
def binarysearch2dArray(n, matrix):
    metaArr = [array[-1] for array in matrix]
    # bisect one side
    # Use the binary search function above
    iO = binarysearch(n, metaArr) 
    
    if iO != len(metaArr):
        array = matrix[iO]
        iT = binarysearch(n, array)
        if iT != len(array) and array[iT] == n:
            return iO, iT

def main():
    print(binarysearch2dArray(4,[[1,2,3],[4,5,6],[7,8,9]]))
    # This one return None, python default Null
    print(binarysearch2dArray(10,[[2,3,4],[5,7,9],[11,12,13],[20,22,24]]))

if __name__ == '__main__':
    main()

    

