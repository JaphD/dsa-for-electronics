import array

my_array = array.array('i', [1,2,3,4,5])


# Using Linear search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 #Means this element is not found in this array
    
print(linear_search(my_array, 5))
