#Good morning! Here's your coding interview problem for today.
#This problem was asked by Uber.
#Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.
#For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
#Follow-up: what if you can't use division?

import collections
import random

# number_list = array of numbers
# Without follow up
def resolve_problem(numbers_list):

	total_mult = 1

	if 0 in numbers_list:

		zero_index = numbers_list.index(0)

		new_vector = numbers_list[:]
		del new_vector[zero_index]

		for number in new_vector:
			total_mult = total_mult * number

		zero_array = [0] * len(numbers_list)

		zero_array[zero_index] = total_mult

		return zero_array

	else:

		for number in numbers_list:
			total_mult = total_mult * number

		new_vector = [total_mult / number for number in numbers_list]	

		return new_vector


def resolve_problem_follow_up(numbers_list):

	new_vector = list()
	total_mult = 1

	for number in numbers_list:
		total_mult = total_mult * number


	new_vector = [total_mult / number for number in numbers_list]	

	return new_vector

if __name__ == '__main__':

	numbers_list = random.sample(range(0, 10), random.randint(1,10))

	print("List: " + str(numbers_list))
	
	#result = resolve_problem([1, 2, 3, 4, 5])
	result = resolve_problem(numbers_list)
	print("Result list:" + str(result))