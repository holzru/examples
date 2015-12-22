def sum_pairs(ints, s):
	result = []
	for count in range(1, len(ints)):
		for i in range(0, count):
			if ints[i] + ints[count] == s and i!=count:
				result.append(ints[i])
				result.append(ints[count])
				break
		if result != []:
			break
	print result if result != [] else None




sum_pairs([1, 4, 7, 3, 15, 16], 8)
sum_pairs([1, -2, 3, 0, -6, 1], -8)
sum_pairs([20, -13, 40], -7)
sum_pairs([1, 2, 3, 4, 1, 0], 6)
sum_pairs([10, 5, 2, 3, 7, 5], 10)
sum_pairs([4, -2, 3, 3, 4], 2)
sum_pairs([0, 2, 0, 1, 3, 5], 7)
sum_pairs([5, 9, 13, 2, -3], 10)
sum_pairs([0, 0, 0, 0, 2], 3)
