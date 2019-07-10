"""
Created by Marina Dunn on 7/9/19
Last edited: 7/9/19
Goal: For a list, sorts elements from smallest to largest value. Will only need to make comparisons for 1
less than overall number of elements in list. Largest value will sort itself towards the end. This is the
concept behind the 'Bubble Sort.'
"""
# below is list of integers that we want to sort from smallest to largest
list = [5, 9, 3, 7, 2] # 5 elements, need to compare 4 and decide if they need to be swapped
swapped = True # creating variable called 'swapped' that will be False if no swaps done, True otherwise

while swapped:
	swapped = False 																					# No swaps done yet
	for i in range(len(list)-1):									# want comparisons for number of elements - 1, in this case, 5 - 1
		if list[i] > list[i + 1]:											# compares elements next to each other
			swapped = True																				 # means that a swap has occurred
			list[i], list[i + 1] = list[i + 1]	# if element to the left is larger, swaps it over to the right

list[i]
print(list[i])																								# prints now sorted list
