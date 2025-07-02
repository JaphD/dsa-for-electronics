import array

arr1 = array.array('i', [1,2,3,4,5,6])

def access_element(array, index):
    if index >= len(array):
        print("There is not any element in this index")

    else:
        print(array[index])

access_element(arr1, 2)  # Accessing the element at index 2


