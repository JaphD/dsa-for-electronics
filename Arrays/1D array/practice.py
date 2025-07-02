from array import *

print("Step 1")
# 1. Create an array and traverse
my_array = array('i', [1,2,3,4,5,6,7])

for i in my_array:
    print(i)

print("Step 2")
# 2. Access individual elements through indexes
print(my_array[0])

print("Step 3")
# 3. Append any value to the array using append() method
my_array.append(5) #appends the value to the end of the array only
print(my_array)

print("Step 4")
# 4. Insert a value in an array using insert() method
my_array.insert(0, 11)
print(my_array)

print("Step 5")
# 5. Extend python array using extend() method
my_array1 = array('i', [10,11,12])
my_array.extend(my_array1) #extends the array by adding the provided array at the end
print(my_array)

print("Step 6")
# 6. Add items from list into array using fromlist() method
temp_list = [20, 21, 22, 23]
my_array.fromlist(temp_list) # similar to extend but we get the elements from a list
print(my_array)

print("Step 7")
# 7. Remove any array element using remove() method
my_array.remove(22) # uses value instead of index. Has O(n) time complexity
print(my_array)

print("Step 8")
# 8. Remove last array element using pop() method
my_array.pop()
print(my_array) # removes the last element. Time efficient process (O(1))

print("Step 9")
# 9. Fetch any element through its index using index() method
print(my_array.index(21)) # prints the fetched index of the provided value

print("Step 10")
# 10. Reverse a python array using reverse() method
my_array.reverse()
print(my_array)

print("Step 11")
# 11. Get array buffer information through buffer_info() method
print(my_array.buffer_info())

print("Step 12")
# 12. Check for number of occurrences of an element using count() method
print(my_array.count(11))

print("Step 13")
# 13. Convert array to a python list with same elements using tolist() method
my_list = my_array.tolist()
print(my_list)

print("Step 14")
# 14. Slice elements from an array
print(my_array[1:4])
print(my_array[:4])
print(my_array[::-1]) # reversing the array



