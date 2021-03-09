"""
Homework 1
Create two lists. The first list should consist of odd numbers. The second list is also of even numbers.
Merge these two lists. Multiply all values in the new list by 2.
Use a loop to print the data type of all values in the new list.

The second solution in case of my miss understanding:

first_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Contains odd numbers
second_list = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]  # Contains even numbers

new_list = first_list + second_list  # Merging the lists
new_list = [i*2 for i in new_list]  # Multiplying all values by 2 in the (new_list)

for j in new_list:
	print(type(j))
"""

first_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # Contains odd numbers
second_list = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]  # Contains even numbers

new_list = first_list + second_list  # Merging the lists

for i in new_list:  # Using for loop to get the values in (new_list)
	i * 2  # Multiplying all values by 2 in the (new_list)
	print(type(i))  # Printing the data types of all values in the (new_list)

	
	
	
