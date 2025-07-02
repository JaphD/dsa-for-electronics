import array

my_array = array.array('i')  # 'i' is the type code for signed integers
my_array = array.array('i', [1, 2, 3, 4, 5])
print(my_array)

# Insertion to the array
my_array.insert(0, 6)
print(my_array)

my_array.insert(2, 6)
print(my_array)

my_array.insert(4, 6)
print(my_array)


