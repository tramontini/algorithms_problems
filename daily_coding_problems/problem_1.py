# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?
import collections
import random

# number_list = array of numbers
# k = sum to be found
def resolve_problem(numbers_list, k):

	passed_numbers = collections.defaultdict()
	index = 0

	for number in numbers_list:
		subtraction = k - number

		if subtraction in passed_numbers.values():
			return True
		else:
			passed_numbers[index] = number
			index += 1

	return False

if __name__ == '__main__':

	k = random.randint(0,50)
	numbers_list = random.sample(range(50), random.randint(3,20))

	print("Number: " + str(k))
	print("List: " + str(numbers_list))
	#result = resolve_problem([10, 15, 3, 7], 17)
	result = resolve_problem(numbers_list, k)
	print(result)