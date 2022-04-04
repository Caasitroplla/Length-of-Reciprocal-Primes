# finds the number of digits until the reciprocal recurses
def find_len_repeating_reciprocal(prime):
	values = []
	remainder = 1
	while len(values) == len(set(values)):
		val = 0
		while val+prime < remainder:
			val += prime
		remainder = (remainder - val) * 10
		values.append(remainder)

	return len(values) - 1
	