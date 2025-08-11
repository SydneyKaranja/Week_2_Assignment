# Empty list
my_list = []

# Adding elements to the list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Printing the list
print("Current list:", my_list)

# Inserting an element at a specific position
my_list.insert(1, 15)  # Insert 15 at index 1
print("List after inserting 15 at index 1:", my_list)

# New list
new_list = [50, 60, 70]

# Extending the current list with new elements
my_list.extend(new_list)
print("List after extending with new elements:", my_list)

# Removing an element from the list
del my_list[-1]  # Remove element at last index
print("List after removing the last element:", my_list)

# Sorting the list in ascending order
my_list.sort()
print("List after sorting in ascending order:", my_list)

# Accessing elements in the list
print("Fourth element:", my_list[3])  # Accessing the fourth element (index 3)



