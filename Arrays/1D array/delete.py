import array

my_array = array.array('i', [0,1,2,3,4,5,6,7])

# Insert the target value to be removed. # Removing the last element is faster
my_array.remove(1)
print(my_array)




