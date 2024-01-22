#!/usr/bin/python3

def safe_print_list(my_list=None, x=0):
	"""Print x elements of a list safely.

	Args:
		my_list (list): The list to print elements from. Defaults to an empty list.
		x (int): The number of elements to print.

	Returns:
		The number of elements successfully printed.
	"""
	elem = 0
	if my_list is None:
		my_list = []

	for i in range(x):
		try:
			print("{}".format(my_list[i]), end="")
			elem += 1
		except IndexError:
			break
	print("")
	return elem
